# 🏠 PLAN DE MIGRACIÓN - INMOBILIARIA APP

## Proyecto Creado Exitosamente
- Ubicación: D:\ESCRITORIO\InmobiliariaApp
- Apps: properties (core adaptado), admin_panel (dashboard adaptado)

## Archivos a Copiar y Adaptar del Proyecto CompuEasys:

### 1. MODELS (properties/models.py)
Adaptar desde core/models.py:
- ProductStore → Property
- Category → PropertyType  
- ProductVariant → PropertyFeatures
- Galeria → PropertyGallery
- SimpleUser → Client
- Pedido → PropertyInquiry/VisitRequest

### 2. VIEWS (properties/views.py)
Copiar y adaptar desde core/views.py:
- store() → properties_list()
- product_detail() → property_detail()
- cart() → favorites()
- add_to_cart() → add_to_favorites()

### 3. TEMPLATES (properties/templates/)
Copiar estructura desde core/templates/:
- store.html → properties.html
- product_detail.html → property_detail.html
- cart.html → favorites.html
- Mantener: navbar, footer

### 4. STATIC FILES
Copiar y adaptar:
- CSS: store.css → properties.css
- JS: store.js → properties.js  
- Mantener: Bootstrap, iconos

### 5. ADMIN PANEL (admin_panel/)
Copiar estructura completa de dashboard/:
- views.py
- urls.py
- templates/admin_panel/
- static/
- Adaptar para gestión de propiedades

### 6. SETTINGS (InmobiliariaApp/settings.py)
Configurar:
- INSTALLED_APPS: ['properties', 'admin_panel']
- MEDIA_ROOT y MEDIA_URL
- STATIC_ROOT y STATIC_URL
- Base de datos SQLite

## Próximos Pasos:
1. ✅ Crear proyecto y apps
2. ⏳ Copiar y adaptar models.py
3. ⏳ Crear migraciones
4. ⏳ Copiar templates adaptados
5. ⏳ Copiar static files
6. ⏳ Configurar URLs
7. ⏳ Adaptar views
8. ⏳ Probar aplicación

