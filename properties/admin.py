from django.contrib import admin
from .models import (
    PropertyType, PropertyStatus, City, Agent, Property, PropertyGallery,
    Client, Favorite, VisitRequest, ContactInquiry, PropertyVisit,
    Auction, Bid, AuctionWatcher, AuctionDeposit, BidHistory
)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PropertyStatus)
class PropertyStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ['name', 'state']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['user__username', 'email', 'phone']

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'city', 'transaction_type', 'status', 'price_sale', 'price_rent', 'is_featured', 'is_active']
    list_filter = ['property_type', 'city', 'status', 'transaction_type', 'is_featured', 'is_active']
    search_fields = ['title', 'address', 'neighborhood']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views_count', 'created_at', 'updated_at']

@admin.register(PropertyGallery)
class PropertyGalleryAdmin(admin.ModelAdmin):
    list_display = ['property', 'title', 'order']
    list_filter = ['property']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email', 'phone']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['client', 'property', 'created_at']
    list_filter = ['created_at']
    search_fields = ['client__name', 'property__title']

@admin.register(VisitRequest)
class VisitRequestAdmin(admin.ModelAdmin):
    list_display = ['client', 'property', 'preferred_date', 'preferred_time', 'status']
    list_filter = ['status', 'preferred_date']
    search_fields = ['client__name', 'property__title']

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'property', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']

@admin.register(PropertyVisit)
class PropertyVisitAdmin(admin.ModelAdmin):
    list_display = ['property', 'ip_address', 'timestamp']
    list_filter = ['timestamp']

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['title', 'property', 'status', 'starting_price', 'current_price', 'start_date', 'end_date', 'total_bids', 'total_bidders']
    list_filter = ['status', 'start_date', 'end_date']
    search_fields = ['title', 'property__title']
    readonly_fields = ['current_price', 'total_bids', 'total_bidders', 'views_count', 'created_at', 'updated_at']

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['auction', 'client', 'amount', 'bid_type', 'is_winning', 'created_at']
    list_filter = ['bid_type', 'is_winning', 'created_at']
    search_fields = ['auction__title', 'client__name']
    readonly_fields = ['created_at']

@admin.register(AuctionWatcher)
class AuctionWatcherAdmin(admin.ModelAdmin):
    list_display = ['auction', 'client', 'notify_new_bid', 'notify_outbid', 'notify_ending_soon']
    list_filter = ['notify_new_bid', 'notify_outbid', 'notify_ending_soon']
    search_fields = ['auction__title', 'client__name']

@admin.register(AuctionDeposit)
class AuctionDepositAdmin(admin.ModelAdmin):
    list_display = ['auction', 'client', 'amount', 'status', 'is_approved', 'created_at']
    list_filter = ['status', 'is_approved', 'created_at']
    search_fields = ['auction__title', 'client__name', 'payment_reference']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(BidHistory)
class BidHistoryAdmin(admin.ModelAdmin):
    list_display = ['auction', 'action', 'previous_price', 'new_price', 'timestamp']
    list_filter = ['action', 'timestamp']
    search_fields = ['auction__title']
    readonly_fields = ['timestamp']
