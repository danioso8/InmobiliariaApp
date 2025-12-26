# 🏠 Empresa G&D Inmobiliario - Sistema Inmobiliario

Sistema completo de gestión inmobiliaria profesional para Empresa G&D Inmobiliario, ubicado en el Edificio Empresarial ISMA, Bello, Colombia.

## 🏢 Información de la Empresa

**Nombre**: Empresa G&D Inmobiliario  
**Ubicación**: CRA 50 # 37-13, Oficina 609, Edificio Empresarial ISMA  
**Ciudad**: Bello, Colombia  
**Teléfono**: +57 301 342 1846  
**Email**: grupo.bienes.raices.j.h@gmail.com  
**Asesor Principal**: Andrés Villegas  
**Horario**: Lunes - Viernes: 8:00 AM - 6:00 PM | Sábados: 9:00 AM - 1:00 PM  

## 🚀 Características

- ✅ Catálogo de propiedades (venta/arriendo)
- ✅ Sistema de subastas en tiempo real
- ✅ Panel administrativo completo
- ✅ Gestión de agentes y clientes
- ✅ Sistema de contacto y solicitudes de visita
- ✅ Galería de imágenes
- ✅ Filtros avanzados de búsqueda
- ✅ Diseño responsive y moderno con glassmorphism
- ✅ Integración con WhatsApp y Google Maps
- ✅ Sección destacada de la oficina con imagen

## 📋 Requisitos

- Python 3.11+
- PostgreSQL (para producción)
- pip

## 🛠️ Instalación Local

1. **Clonar el repositorio**
```bash
git clone <tu-repositorio>
cd InmobiliariaApp
```

2. **Crear entorno virtual**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Guardar la imagen del edificio**
```bash
# Opción 1: Usar el script automático
python copiar_imagen_edificio.py

# Opción 2: Manual - Guarda la imagen del Edificio ISMA como:
# properties/static/img/edificio-isma.jpg
```

5. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

6. **Aplicar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

Visita: http://127.0.0.1:8000/

## 🌐 Deployment en Render

### Opción 1: Usando render.yaml (Recomendado)

1. **Conectar tu repositorio a Render**
   - Ve a https://dashboard.render.com/
   - Click en "New +" → "Blueprint"
   - Conecta tu repositorio de GitHub

2. **Render detectará automáticamente el archivo `render.yaml`**
   - Creará la base de datos PostgreSQL
   - Configurará el servicio web
   - Aplicará las migraciones

3. **Configurar variables de entorno adicionales (opcional)**
   - `SECRET_KEY`: Se genera automáticamente
   - `DATABASE_URL`: Se conecta automáticamente
   - `DEBUG`: False (por defecto)

### Opción 2: Configuración Manual

1. **Crear Base de Datos PostgreSQL**
   - New → PostgreSQL
   - Name: `inmobiliariaapp-db`
   - Plan: Free

2. **Crear Web Service**
   - New → Web Service
   - Conectar repositorio
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn InmobiliariaApp.wsgi:application`

3. **Variables de Entorno**
   ```
   PYTHON_VERSION=3.11.0
   DATABASE_URL=[Auto-conectado desde PostgreSQL]
   SECRET_KEY=[Generar una clave segura]
   DEBUG=False
   ALLOWED_HOSTS=.render.com
   ```

## 📦 Estructura del Proyecto

```
InmobiliariaApp/
├── InmobiliariaApp/          # Configuración del proyecto
│   ├── settings.py          # Configuraciones
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # WSGI para deployment
├── properties/              # App de propiedades
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas
│   ├── admin.py            # Configuración admin
│   └── templates/          # Templates HTML
├── admin_panel/            # Panel administrativo
├── static/                 # Archivos estáticos
├── media_files/           # Archivos subidos
├── build.sh               # Script de build para Render
├── render.yaml            # Configuración de Render
├── requirements.txt       # Dependencias Python
└── .env.example          # Ejemplo de variables de entorno
```

## 🔐 Credenciales por Defecto

**Admin Django:**
- Usuario: `admin`
- Contraseña: `admin123`

⚠️ **IMPORTANTE**: Cambiar estas credenciales en producción.

## 🎨 Tecnologías Utilizadas

- **Backend**: Django 4.2.24
- **Base de Datos**: PostgreSQL / SQLite (desarrollo)
- **Frontend**: Bootstrap 5.3, HTML5, CSS3
- **Servidor**: Gunicorn
- **Archivos Estáticos**: WhiteNoise
- **Imágenes**: Pillow, Cloudinary (opcional)

## 📝 Notas Importantes

### Base de Datos
- **Desarrollo**: SQLite (automático)
- **Producción**: PostgreSQL (Render provee una gratis por 90 días)
- La base de datos de producción es **completamente independiente** de tu base de datos local

### Archivos Media
- En desarrollo se guardan en `/media_files/`
- Para producción se recomienda usar Cloudinary o S3
- Configurar variables de entorno para Cloudinary si deseas usarlo

### Migraciones
- Las migraciones se aplican automáticamente en el deployment
- El superusuario se crea automáticamente si no existe

## 🐛 Troubleshooting

**Error: "django.db.utils.OperationalError"**
- Verificar que la variable `DATABASE_URL` esté configurada correctamente
- Asegurarse de que la base de datos PostgreSQL esté activa en Render

**Error: "Static files not found"**
- Ejecutar: `python manage.py collectstatic`
- Verificar que WhiteNoise esté en MIDDLEWARE

**Error: "This site can't provide a secure connection"**
- Render tarda unos minutos en provisionar el certificado SSL
- Esperar 5-10 minutos después del primer deployment

## 📧 Contacto

Para soporte o consultas sobre el proyecto, contactar al equipo de Empresa G&D Inmobiliario.

## 📄 Licencia

Este proyecto es privado y confidencial.
