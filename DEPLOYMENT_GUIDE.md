# 🚀 GUÍA PASO A PASO PARA SUBIR A RENDER

## ✅ Archivos ya configurados:
- ✅ `build.sh` - Script de construcción
- ✅ `render.yaml` - Configuración automática
- ✅ `runtime.txt` - Versión de Python
- ✅ `.env.example` - Ejemplo de variables
- ✅ `.gitignore` - Archivos a ignorar
- ✅ `settings.py` - Configurado para producción
- ✅ `requirements.txt` - Dependencias

---

## 📝 PASOS PARA EL DEPLOYMENT

### 1️⃣ Preparar el Repositorio Git

```bash
# Inicializar Git (si no está inicializado)
git init

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Preparar proyecto para deployment en Render"

# Crear repositorio en GitHub y conectar
git remote add origin https://github.com/tu-usuario/tu-repositorio.git
git branch -M main
git push -u origin main
```

### 2️⃣ Configurar en Render

1. **Ir a Render Dashboard**
   - Visita: https://dashboard.render.com/
   - Inicia sesión con tu cuenta

2. **Crear desde Blueprint (Opción Automática - RECOMENDADA)**
   - Click en "New +" en el dashboard
   - Selecciona "Blueprint"
   - Conecta tu repositorio de GitHub
   - Render detectará automáticamente `render.yaml`
   - Click en "Apply"
   - ✨ ¡Render configurará todo automáticamente!

   **O**

3. **Configuración Manual (Opción Alternativa)**

   **a) Crear Base de Datos PostgreSQL**
   - Click en "New +" → "PostgreSQL"
   - Name: `inmobiliariaapp-db`
   - Database: `inmobiliariaapp`
   - User: `inmobiliariaapp_user`
   - Region: Oregon (US West) - o el más cercano
   - Plan: **Free** (90 días gratis)
   - Click en "Create Database"
   - **⏰ Esperar 2-5 minutos** hasta que esté "Available"

   **b) Crear Web Service**
   - Click en "New +" → "Web Service"
   - Connect repository → Selecciona tu repositorio
   - Name: `inmobiliariaapp`
   - Region: Mismo que la base de datos
   - Branch: `main`
   - Runtime: Python 3
   - Build Command: `./build.sh`
   - Start Command: `gunicorn InmobiliariaApp.wsgi:application`
   - Plan: **Free** (750 horas/mes gratis)

   **c) Configurar Variables de Entorno**
   En la sección "Environment Variables":
   ```
   PYTHON_VERSION = 3.11.0
   SECRET_KEY = [Click en "Generate" para generar una clave segura]
   DEBUG = False
   ALLOWED_HOSTS = .render.com
   DATABASE_URL = [Seleccionar tu base de datos PostgreSQL]
   ```

   **d) Deploy**
   - Click en "Create Web Service"
   - ⏰ El primer deployment tarda 5-10 minutos

---

## 🔍 Verificar el Deployment

### Durante el Build
Verás estos logs en Render:
```
==> Cloning from https://github.com/...
==> Running build command './build.sh'
==> Installing dependencies from requirements.txt
==> Collecting static files
==> Running migrations
==> Creating superuser
==> Build successful!
==> Starting service with 'gunicorn...'
==> Your service is live 🎉
```

### URLs Generadas
Render te dará una URL como:
```
https://inmobiliariaapp.onrender.com
```

### Probar la Aplicación
1. **Página Principal**: https://tu-app.onrender.com/
2. **Admin Django**: https://tu-app.onrender.com/admin/
3. **Panel Admin**: https://tu-app.onrender.com/admin_panel/

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `admin123`

⚠️ **CAMBIAR ESTAS CREDENCIALES INMEDIATAMENTE EN PRODUCCIÓN**

---

## 🛠️ Configuraciones Post-Deployment

### 1. Cambiar Credenciales de Admin
```bash
# Conectar a la shell de Django en Render
# En Render Dashboard → Tu servicio → Shell

python manage.py changepassword admin
```

### 2. Configurar Dominio Personalizado (Opcional)
- En Render Dashboard → Settings → Custom Domain
- Agregar tu dominio: `www.tudominio.com`
- Configurar DNS según instrucciones de Render

### 3. Configurar Cloudinary para Imágenes (Opcional)
Si quieres usar Cloudinary para almacenar imágenes:

1. Crear cuenta en https://cloudinary.com/
2. Obtener credenciales
3. Agregar variables de entorno en Render:
   ```
   CLOUDINARY_CLOUD_NAME = tu-cloud-name
   CLOUDINARY_API_KEY = tu-api-key
   CLOUDINARY_API_SECRET = tu-api-secret
   ```

---

## 🐛 Troubleshooting

### Error: "Application failed to respond"
**Causa**: El servidor no está levantando correctamente
**Solución**:
1. Revisar logs en Render Dashboard
2. Verificar que `gunicorn` esté en requirements.txt
3. Verificar el comando de start: `gunicorn InmobiliariaApp.wsgi:application`

### Error: "django.db.utils.OperationalError"
**Causa**: No se puede conectar a la base de datos
**Solución**:
1. Verificar que la variable `DATABASE_URL` esté configurada
2. Asegurarse de que la base de datos PostgreSQL esté "Available"
3. Esperar 5 minutos después de crear la BD

### Error: "Static files not found"
**Causa**: Archivos estáticos no se recolectaron
**Solución**:
1. Verificar que `./build.sh` tenga permisos de ejecución
2. En el build command debe aparecer "Collecting static files"
3. Verificar que WhiteNoise esté en MIDDLEWARE

### Sitio muy lento o se "duerme"
**Causa**: Plan gratuito se duerme después de 15 minutos de inactividad
**Solución**:
- Primera visita tarda 30-60 segundos en "despertar"
- Opción 1: Actualizar a plan de pago ($7/mes)
- Opción 2: Usar un servicio de ping (UptimeRobot) para mantenerlo activo

### SSL Certificate Error
**Causa**: Render está provisionando el certificado SSL
**Solución**: Esperar 5-10 minutos después del primer deployment

---

## 📊 Monitoreo y Mantenimiento

### Ver Logs en Tiempo Real
1. Ir a Render Dashboard
2. Seleccionar tu servicio
3. Click en "Logs"
4. Puedes filtrar por errores o búsquedas específicas

### Base de Datos PostgreSQL Gratis
⚠️ **IMPORTANTE**: 
- El plan gratuito de PostgreSQL es por **90 días**
- Después de 90 días:
  - Opción 1: Actualizar a plan de pago ($7/mes)
  - Opción 2: Crear nueva base de datos y migrar datos
  - Opción 3: Usar otro servicio (ElephantSQL, etc.)

### Hacer Backup de la Base de Datos
```bash
# Desde tu computadora local (necesitas psql instalado)
pg_dump [DATABASE_URL] > backup.sql

# O desde Render Shell
python manage.py dumpdata > backup.json
```

---

## 🎯 Checklist Final

Antes de considerar el deployment completo:

- [ ] Proyecto subido a GitHub
- [ ] Base de datos PostgreSQL creada y "Available"
- [ ] Web Service creado con variables de entorno configuradas
- [ ] Build completado exitosamente (sin errores en logs)
- [ ] Página principal carga correctamente
- [ ] Admin Django accesible (/admin/)
- [ ] Credenciales de admin cambiadas
- [ ] SSL activo (https://)
- [ ] Archivos estáticos cargando correctamente
- [ ] Base de datos independiente de la local ✅

---

## 📞 Soporte

Si encuentras algún problema:
1. Revisar logs en Render Dashboard
2. Verificar la documentación oficial: https://render.com/docs
3. Consultar el README.md del proyecto

---

## 🎉 ¡Felicidades!

Tu aplicación de Empresa G&D Inmobiliario ahora está en producción con:
- ✅ Base de datos PostgreSQL independiente
- ✅ Archivos estáticos optimizados con WhiteNoise
- ✅ SSL/HTTPS automático
- ✅ Deployment automático desde Git
- ✅ Configuraciones de seguridad aplicadas

**URL de tu aplicación**: https://tu-app.onrender.com

¡Disfruta de tu aplicación en la nube! 🚀
