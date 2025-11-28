from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# ========================================
# MODELOS PARA INMOBILIARIA
# ========================================

class PropertyType(models.Model):
    """Tipos de propiedad: Casa, Apartamento, Local, Lote, etc."""
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    icon = models.CharField(max_length=50, default="bi-house", verbose_name="Ícono Bootstrap")
    
    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipos de Propiedades"
        ordering = ["name"]
    
    def __str__(self):
        return self.name


class PropertyStatus(models.Model):
    """Estado de la propiedad: Disponible, Vendida, Arrendada, etc."""
    name = models.CharField(max_length=50, verbose_name="Estado")
    slug = models.SlugField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default="#10b981", verbose_name="Color hex")
    
    class Meta:
        verbose_name = "Estado de Propiedad"
        verbose_name_plural = "Estados de Propiedades"
    
    def __str__(self):
        return self.name


class City(models.Model):
    """Ciudades donde hay propiedades"""
    name = models.CharField(max_length=100, verbose_name="Ciudad")
    state = models.CharField(max_length=100, verbose_name="Departamento")
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["name"]
    
    def __str__(self):
        return f"{self.name}, {self.state}"


class Agent(models.Model):
    """Agentes inmobiliarios"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agent_profile")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email")
    photo = models.ImageField(upload_to="agents/", blank=True, null=True, verbose_name="Foto")
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name="WhatsApp")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Agente Inmobiliario"
        verbose_name_plural = "Agentes Inmobiliarios"
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"


class Property(models.Model):
    """Modelo principal de propiedades"""
    TRANSACTION_TYPES = [
        ("sale", "Venta"),
        ("rent", "Arriendo"),
        ("auction", "Subasta"),
        ("both", "Venta y Arriendo")
    ]
    
    # Información básica
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(verbose_name="Descripción")
    property_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT, related_name="properties", verbose_name="Tipo")
    status = models.ForeignKey(PropertyStatus, on_delete=models.PROTECT, related_name="properties", verbose_name="Estado")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default="sale", verbose_name="Tipo de Transacción")
    
    # Ubicación
    address = models.CharField(max_length=255, verbose_name="Dirección")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="properties", verbose_name="Ciudad")
    neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Barrio")
    zip_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Código Postal")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitud")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitud")
    
    # Características
    bedrooms = models.PositiveIntegerField(default=0, verbose_name="Habitaciones")
    bathrooms = models.PositiveIntegerField(default=0, verbose_name="Baños")
    area_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Área Total (m²)")
    area_built = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Área Construida (m²)")
    floors = models.PositiveIntegerField(default=1, verbose_name="Pisos")
    parking_spaces = models.PositiveIntegerField(default=0, verbose_name="Parqueaderos")
    age_years = models.PositiveIntegerField(blank=True, null=True, verbose_name="Antigüedad (años)")
    
    # Precios
    price_sale = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Precio Venta")
    price_rent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Precio Arriendo")
    price_admin = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Administración")
    
    # Características adicionales
    has_pool = models.BooleanField(default=False, verbose_name="Piscina")
    has_gym = models.BooleanField(default=False, verbose_name="Gimnasio")
    has_garden = models.BooleanField(default=False, verbose_name="Jardín")
    has_balcony = models.BooleanField(default=False, verbose_name="Balcón")
    has_elevator = models.BooleanField(default=False, verbose_name="Ascensor")
    has_security = models.BooleanField(default=False, verbose_name="Vigilancia")
    is_furnished = models.BooleanField(default=False, verbose_name="Amoblado")
    allows_pets = models.BooleanField(default=False, verbose_name="Acepta Mascotas")
    
    # Imágenes
    main_image = models.ImageField(upload_to="properties/", verbose_name="Imagen Principal")
    
    # Relaciones
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name="properties", verbose_name="Agente")
    
    # Metadata
    is_featured = models.BooleanField(default=False, verbose_name="Destacada")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Vistas")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizada")
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    
    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["city", "property_type"]),
            models.Index(fields=["price_sale"]),
            models.Index(fields=["price_rent"]),
        ]
    
    def __str__(self):
        return self.title
    
    def get_price(self):
        """Retorna el precio según el tipo de transacción"""
        if self.transaction_type == "sale":
            return self.price_sale
        elif self.transaction_type == "rent":
            return self.price_rent
        return self.price_sale or self.price_rent


class PropertyGallery(models.Model):
    """Galería de fotos de propiedades"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="gallery", verbose_name="Propiedad")
    image = models.ImageField(upload_to="properties/gallery/", verbose_name="Imagen")
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Título")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Foto de Galería"
        verbose_name_plural = "Galería de Fotos"
        ordering = ["order", "created_at"]
    
    def __str__(self):
        return f"Foto de {self.property.title}"


class Client(models.Model):
    """Clientes/Usuarios del sistema"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="client_profile")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Propiedades favoritas de los usuarios"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="favorites", verbose_name="Cliente")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="favorited_by", verbose_name="Propiedad")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ["client", "property"]
    
    def __str__(self):
        return f"{self.client.name} - {self.property.title}"


class VisitRequest(models.Model):
    """Solicitudes de visitas a propiedades"""
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("confirmed", "Confirmada"),
        ("completed", "Completada"),
        ("cancelled", "Cancelada")
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="visit_requests", verbose_name="Propiedad")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="visit_requests", verbose_name="Cliente")
    preferred_date = models.DateField(verbose_name="Fecha Preferida")
    preferred_time = models.TimeField(verbose_name="Hora Preferida")
    message = models.TextField(blank=True, null=True, verbose_name="Mensaje")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Estado")
    agent_notes = models.TextField(blank=True, null=True, verbose_name="Notas del Agente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Solicitud de Visita"
        verbose_name_plural = "Solicitudes de Visitas"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.client.name} - {self.property.title} ({self.get_status_display()})"


class ContactInquiry(models.Model):
    """Consultas generales de contacto"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True, related_name="inquiries", verbose_name="Propiedad")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    message = models.TextField(verbose_name="Mensaje")
    is_read = models.BooleanField(default=False, verbose_name="Leído")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Consulta de Contacto"
        verbose_name_plural = "Consultas de Contacto"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"


class PropertyVisit(models.Model):
    """Registro de visitas a propiedades (analytics)"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="visits", verbose_name="Propiedad")
    session_key = models.CharField(max_length=40, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Visita a Propiedad"
        verbose_name_plural = "Visitas a Propiedades"
    
    def __str__(self):
        return f"Visita a {self.property.title}"


# ========================================
# SISTEMA DE SUBASTAS
# ========================================

class Auction(models.Model):
    """Subastas de propiedades"""
    STATUS_CHOICES = [
        ("draft", "Borrador"),
        ("scheduled", "Programada"),
        ("active", "Activa"),
        ("ended", "Finalizada"),
        ("cancelled", "Cancelada")
    ]
    
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="auction", verbose_name="Propiedad")
    title = models.CharField(max_length=200, verbose_name="Título de Subasta")
    description = models.TextField(verbose_name="Descripción")
    
    # Precios y parámetros
    starting_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio Inicial")
    reserve_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Precio de Reserva")
    current_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio Actual")
    min_bid_increment = models.DecimalField(max_digits=10, decimal_places=2, default=1000, verbose_name="Incremento Mínimo de Puja")
    buy_now_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Precio Compra Ya")
    
    # Fechas y tiempos
    start_date = models.DateTimeField(verbose_name="Fecha de Inicio")
    end_date = models.DateTimeField(verbose_name="Fecha de Finalización")
    auto_extend = models.BooleanField(default=True, verbose_name="Extensión Automática")
    extend_minutes = models.PositiveIntegerField(default=5, verbose_name="Minutos de Extensión")
    
    # Estado y ganador
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft", verbose_name="Estado")
    winner = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_auctions", verbose_name="Ganador")
    winning_bid = models.ForeignKey("Bid", on_delete=models.SET_NULL, null=True, blank=True, related_name="won_auction", verbose_name="Puja Ganadora")
    
    # Configuración
    require_deposit = models.BooleanField(default=False, verbose_name="Requiere Depósito")
    deposit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Monto de Depósito")
    allow_proxy_bidding = models.BooleanField(default=True, verbose_name="Permitir Pujas Automáticas")
    
    # Metadata
    total_bids = models.PositiveIntegerField(default=0, verbose_name="Total de Pujas")
    total_bidders = models.PositiveIntegerField(default=0, verbose_name="Total de Participantes")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Vistas")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizada")
    
    class Meta:
        verbose_name = "Subasta"
        verbose_name_plural = "Subastas"
        ordering = ["-start_date"]
        indexes = [
            models.Index(fields=["status", "start_date"]),
            models.Index(fields=["end_date"]),
        ]
    
    def __str__(self):
        return f"Subasta: {self.title}"
    
    def is_active(self):
        """Verifica si la subasta está activa"""
        now = timezone.now()
        return self.status == "active" and self.start_date <= now <= self.end_date
    
    def time_remaining(self):
        """Calcula el tiempo restante"""
        if self.status != "active":
            return None
        now = timezone.now()
        if now > self.end_date:
            return timedelta(0)
        return self.end_date - now
    
    def can_bid(self, client):
        """Verifica si un cliente puede pujar"""
        if not self.is_active():
            return False, "La subasta no está activa"
        if self.require_deposit:
            try:
                deposit = AuctionDeposit.objects.get(auction=self, client=client, is_approved=True)
            except AuctionDeposit.DoesNotExist:
                return False, "Requiere depósito aprobado"
        return True, ""


class Bid(models.Model):
    """Pujas en subastas"""
    BID_TYPES = [
        ("manual", "Manual"),
        ("proxy", "Automática"),
        ("buy_now", "Compra Ya")
    ]
    
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids", verbose_name="Subasta")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="bids", verbose_name="Cliente")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto")
    bid_type = models.CharField(max_length=20, choices=BID_TYPES, default="manual", verbose_name="Tipo de Puja")
    
    # Para pujas automáticas
    max_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Monto Máximo Automático")
    is_proxy_active = models.BooleanField(default=False, verbose_name="Puja Automática Activa")
    
    # Metadata
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name="IP")
    user_agent = models.TextField(blank=True, null=True, verbose_name="User Agent")
    is_winning = models.BooleanField(default=False, verbose_name="Es Ganadora")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    
    class Meta:
        verbose_name = "Puja"
        verbose_name_plural = "Pujas"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["auction", "-amount"]),
            models.Index(fields=["client", "-created_at"]),
        ]
    
    def __str__(self):
        return f"{self.client.name} - ${self.amount:,.0f} en {self.auction.title}"
    
    def save(self, *args, **kwargs):
        """Actualiza el precio actual de la subasta"""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            # Actualizar precio actual de la subasta
            self.auction.current_price = self.amount
            self.auction.total_bids += 1
            
            # Marcar todas las otras pujas como no ganadoras
            Bid.objects.filter(auction=self.auction).exclude(pk=self.pk).update(is_winning=False)
            self.is_winning = True
            
            # Actualizar conteo de participantes únicos
            unique_bidders = Bid.objects.filter(auction=self.auction).values("client").distinct().count()
            self.auction.total_bidders = unique_bidders
            
            self.auction.save()
            super().save(update_fields=["is_winning"])


class AuctionWatcher(models.Model):
    """Usuarios que siguen una subasta"""
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="watchers", verbose_name="Subasta")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="watched_auctions", verbose_name="Cliente")
    notify_new_bid = models.BooleanField(default=True, verbose_name="Notificar Nueva Puja")
    notify_outbid = models.BooleanField(default=True, verbose_name="Notificar al ser Superado")
    notify_ending_soon = models.BooleanField(default=True, verbose_name="Notificar Próximo a Finalizar")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Seguidor de Subasta"
        verbose_name_plural = "Seguidores de Subastas"
        unique_together = ["auction", "client"]
    
    def __str__(self):
        return f"{self.client.name} sigue {self.auction.title}"


class AuctionDeposit(models.Model):
    """Depósitos para participar en subastas"""
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("approved", "Aprobado"),
        ("rejected", "Rechazado"),
        ("refunded", "Reembolsado")
    ]
    
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="deposits", verbose_name="Subasta")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="auction_deposits", verbose_name="Cliente")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Monto")
    payment_method = models.CharField(max_length=50, verbose_name="Método de Pago")
    payment_reference = models.CharField(max_length=100, blank=True, null=True, verbose_name="Referencia de Pago")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Estado")
    is_approved = models.BooleanField(default=False, verbose_name="Aprobado")
    
    proof_of_payment = models.ImageField(upload_to="auction_deposits/", blank=True, null=True, verbose_name="Comprobante")
    admin_notes = models.TextField(blank=True, null=True, verbose_name="Notas del Admin")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Depósito de Subasta"
        verbose_name_plural = "Depósitos de Subastas"
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Depósito {self.client.name} - {self.auction.title}"


class BidHistory(models.Model):
    """Historial detallado de pujas para auditoría"""
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bid_history", verbose_name="Subasta")
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="history", verbose_name="Puja")
    action = models.CharField(max_length=50, verbose_name="Acción")
    previous_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio Anterior")
    new_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio Nuevo")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    
    class Meta:
        verbose_name = "Historial de Puja"
        verbose_name_plural = "Historial de Pujas"
        ordering = ["-timestamp"]
    
    def __str__(self):
        return f"{self.action} - {self.auction.title}"
