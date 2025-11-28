from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import (
    Property, PropertyType, City, PropertyStatus, 
    Agent, ContactInquiry, Auction, Bid
)

# ========================================
# VISTAS PÚBLICAS
# ========================================

def home(request):
    """Página principal"""
    featured_properties = Property.objects.filter(
        is_active=True, 
        is_featured=True
    ).select_related('city', 'property_type', 'status')[:6]
    
    # Propiedades recientes
    recent_properties = Property.objects.filter(
        is_active=True
    ).select_related('city', 'property_type', 'status').order_by('-created_at')[:6]
    
    # Tipos de propiedades con conteo
    property_types = PropertyType.objects.annotate(
        count=Count('properties', filter=Q(properties__is_active=True))
    )
    
    # Ciudades con propiedades
    cities = City.objects.annotate(
        count=Count('properties', filter=Q(properties__is_active=True))
    ).filter(count__gt=0)[:6]
    
    context = {
        'featured_properties': featured_properties,
        'recent_properties': recent_properties,
        'property_types': property_types,
        'cities': cities,
    }
    return render(request, 'properties/home.html', context)


class PropertyListView(ListView):
    """Listado de propiedades con filtros"""
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Property.objects.filter(is_active=True).select_related(
            'city', 'property_type', 'status', 'agent'
        )
        
        # Filtros
        transaction_type = self.request.GET.get('transaction_type')
        property_type = self.request.GET.get('property_type')
        city = self.request.GET.get('city')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        bedrooms = self.request.GET.get('bedrooms')
        search = self.request.GET.get('search')
        
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
        
        if property_type:
            queryset = queryset.filter(property_type__slug=property_type)
        
        if city:
            queryset = queryset.filter(city__slug=city)
        
        if min_price:
            queryset = queryset.filter(
                Q(price_sale__gte=min_price) | Q(price_rent__gte=min_price)
            )
        
        if max_price:
            queryset = queryset.filter(
                Q(price_sale__lte=max_price) | Q(price_rent__lte=max_price)
            )
        
        if bedrooms:
            queryset = queryset.filter(bedrooms__gte=bedrooms)
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search) |
                Q(address__icontains=search) |
                Q(neighborhood__icontains=search)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_types'] = PropertyType.objects.all()
        context['cities'] = City.objects.all()
        context['filters'] = self.request.GET
        return context


class PropertyDetailView(DetailView):
    """Detalle de una propiedad"""
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'
    
    def get_object(self):
        property_obj = get_object_or_404(
            Property.objects.select_related('city', 'property_type', 'status', 'agent'),
            slug=self.kwargs['slug'],
            is_active=True
        )
        
        # Incrementar contador de vistas
        property_obj.views_count += 1
        property_obj.save(update_fields=['views_count'])
        
        return property_obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Propiedades similares
        similar_properties = Property.objects.filter(
            property_type=self.object.property_type,
            city=self.object.city,
            is_active=True
        ).exclude(id=self.object.id)[:4]
        
        context['similar_properties'] = similar_properties
        context['gallery'] = self.object.gallery.all()
        
        return context


def contact_inquiry(request):
    """Procesar formulario de contacto"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        property_id = request.POST.get('property_id')
        
        inquiry = ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            property_id=property_id if property_id else None
        )
        
        # TODO: Enviar notificación por email
        
        return redirect('properties:contact_success')
    
    return render(request, 'properties/contact.html')


def contact_success(request):
    """Página de éxito al enviar contacto"""
    return render(request, 'properties/contact_success.html')


# ========================================
# VISTAS DE SUBASTAS
# ========================================

class AuctionListView(ListView):
    """Listado de subastas activas"""
    model = Auction
    template_name = 'properties/auction_list.html'
    context_object_name = 'auctions'
    paginate_by = 12
    
    def get_queryset(self):
        return Auction.objects.filter(
            status='active'
        ).select_related('property', 'property__city', 'property__property_type')


class AuctionDetailView(DetailView):
    """Detalle de una subasta"""
    model = Auction
    template_name = 'properties/auction_detail.html'
    context_object_name = 'auction'
    
    def get_object(self):
        auction = get_object_or_404(
            Auction.objects.select_related('property', 'property__agent'),
            pk=self.kwargs['pk']
        )
        
        # Incrementar contador de vistas
        auction.views_count += 1
        auction.save(update_fields=['views_count'])
        
        return auction
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Últimas pujas
        context['recent_bids'] = self.object.bids.select_related('client')[:10]
        context['total_bids'] = self.object.bids.count()
        
        return context
