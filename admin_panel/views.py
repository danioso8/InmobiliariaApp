from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum, Avg, Q
from django.utils import timezone
from datetime import timedelta
from properties.models import (
    Property, ContactInquiry, VisitRequest, 
    Auction, Bid, Agent, Client
)

def is_staff_or_agent(user):
    """Verifica si el usuario es staff o agente"""
    return user.is_staff or hasattr(user, 'agent_profile')

@login_required
@user_passes_test(is_staff_or_agent)
def dashboard(request):
    """Panel de control principal"""
    
    # Estadísticas generales
    total_properties = Property.objects.filter(is_active=True).count()
    total_agents = Agent.objects.filter(is_active=True).count()
    total_clients = Client.objects.count()
    pending_inquiries = ContactInquiry.objects.filter(is_read=False).count()
    pending_visits = VisitRequest.objects.filter(status='pending').count()
    
    # Propiedades por estado
    properties_by_status = Property.objects.filter(
        is_active=True
    ).values('status__name').annotate(count=Count('id'))
    
    # Propiedades recientes
    recent_properties = Property.objects.filter(
        is_active=True
    ).select_related('city', 'property_type', 'status', 'agent').order_by('-created_at')[:5]
    
    # Consultas recientes
    recent_inquiries = ContactInquiry.objects.select_related(
        'property'
    ).order_by('-created_at')[:5]
    
    # Visitas pendientes
    pending_visit_requests = VisitRequest.objects.filter(
        status='pending'
    ).select_related('property', 'client').order_by('-created_at')[:5]
    
    # Subastas activas
    active_auctions = Auction.objects.filter(
        status='active'
    ).select_related('property').order_by('-start_date')[:5]
    
    context = {
        'total_properties': total_properties,
        'total_agents': total_agents,
        'total_clients': total_clients,
        'pending_inquiries': pending_inquiries,
        'pending_visits': pending_visits,
        'properties_by_status': properties_by_status,
        'recent_properties': recent_properties,
        'recent_inquiries': recent_inquiries,
        'pending_visit_requests': pending_visit_requests,
        'active_auctions': active_auctions,
    }
    
    return render(request, 'admin_panel/dashboard.html', context)
