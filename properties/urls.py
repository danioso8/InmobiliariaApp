from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Propiedades
    path('properties/', views.PropertyListView.as_view(), name='property_list'),
    path('property/<slug:slug>/', views.PropertyDetailView.as_view(), name='property_detail'),
    
    # Contacto
    path('contact/', views.contact_inquiry, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    
    # Subastas
    path('auctions/', views.AuctionListView.as_view(), name='auction_list'),
    path('auction/<int:pk>/', views.AuctionDetailView.as_view(), name='auction_detail'),
]
