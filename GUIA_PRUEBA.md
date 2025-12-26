# 🏢 Empresa G&D Inmobiliario - Guía Rápida de Prueba

## 🎯 ¿Qué se ha actualizado?

Tu aplicación web de Empresa G&D Inmobiliario ha sido completamente modernizada con:

✅ **Ubicación actualizada**: Edificio Empresarial ISMA, Oficina 609  
✅ **Contacto actualizado**: +57 301 342 1846  
✅ **Asesor destacado**: Andrés Villegas  
✅ **Diseño modernizado**: Landing page con efectos glassmorphism y animaciones  
✅ **Nueva sección**: Información del edificio con imagen  
✅ **Página de contacto mejorada**: Formulario y mapa integrado  

---

## 🚀 Cómo Probar los Cambios

### Paso 1: Guardar la Imagen del Edificio (IMPORTANTE)

La imagen del Edificio Empresarial ISMA que adjuntaste debe guardarse manualmente:

**Opción A - Script Automático:**
```bash
python copiar_imagen_edificio.py
```

**Opción B - Manual:**
1. Descarga la imagen del edificio del chat
2. Renómbrala como: `edificio-isma.jpg`
3. Guárdala en: `d:\ESCRITORIO\InmobiliariaApp\properties\static\img\`

### Paso 2: Iniciar el Servidor de Desarrollo

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python manage.py runserver
```

### Paso 3: Ver la Aplicación

Abre tu navegador y visita:
```
http://localhost:8000
```

---

## 📋 Checklist de Verificación

### Página Principal (Home)
- [ ] El hero muestra "Tu Hogar Ideal Te Espera"
- [ ] Se muestra la información de Andrés Villegas con teléfono 301 342 1846
- [ ] La sección de estadísticas muestra: 350+, 800+, 6+, 100%
- [ ] Aparece la nueva sección "Visítanos en el Edificio Empresarial ISMA"
- [ ] La imagen del edificio se ve correctamente
- [ ] Los badges de información muestran:
  - Edificio Empresarial ISMA - Oficina 609
  - CRA 50 # 37-13, Bello, Colombia
  - +57 301 342 1846
  - Andrés Villegas - Especialista Inmobiliario
- [ ] El botón "Ver en Google Maps" funciona
- [ ] La sección "Por Qué Elegirnos" menciona Bello y el Edificio ISMA
- [ ] El CTA final muestra el teléfono y ubicación

### Footer (Todas las Páginas)
- [ ] Muestra "CRA 50 # 37-13 Oficina 609"
- [ ] Muestra "Edificio Empresarial ISMA"
- [ ] Muestra "Bello, Colombia"
- [ ] Muestra "+57 301 342 1846"
- [ ] Muestra "Asesor: Andrés Villegas"

### Página de Contacto
- [ ] Hero section con gradiente azul
- [ ] Formulario de contacto modernizado
- [ ] Panel lateral con 6 tarjetas de información:
  1. Oficina (Edificio ISMA, Oficina 609)
  2. Dirección (CRA 50 # 37-13, Bello)
  3. Teléfono (+57 301 342 1846)
  4. Asesor (Andrés Villegas)
  5. Email (grupo.bienes.raices.j.h@gmail.com)
  6. Horario (Lun-Vie 8am-6pm, Sáb 9am-1pm)
- [ ] Botón de WhatsApp funcional
- [ ] Mapa de Google Maps embebido

### Diseño Responsive
- [ ] Prueba en móvil (F12 -> modo responsive)
- [ ] Todos los elementos se adaptan correctamente
- [ ] Los botones son clickeables en móvil

---

## 🎨 Características Nuevas para Probar

### 1. Efectos de Hover
- Pasa el mouse sobre las tarjetas de estadísticas
- Pasa el mouse sobre las tarjetas de información de contacto
- Pasa el mouse sobre la imagen del edificio

### 2. Animaciones
- Recarga la página principal para ver las animaciones de entrada del hero
- Las tarjetas deben "flotar" ligeramente al hacer hover

### 3. Enlaces Funcionales
- **WhatsApp**: Click en el botón verde de WhatsApp
- **Teléfono**: Click en el número de teléfono (debe abrir la app de llamadas)
- **Email**: Click en el email (debe abrir el cliente de correo)
- **Google Maps**: Click en "Ver en Google Maps"

---

## 📱 Integración de WhatsApp

El botón de WhatsApp está configurado con el número: **+57 301 342 1846**

Para probarlo:
1. Click en el botón "Chatea por WhatsApp" o "Contáctanos por WhatsApp"
2. Se abrirá WhatsApp Web o la app de WhatsApp
3. Iniciará una conversación con el número de la inmobiliaria

---

## 🗺️ Integración de Google Maps

La dirección está configurada como: **CRA 50 # 37-13, Bello, Colombia**

Para probar:
1. Ve a la página de contacto
2. Verás un mapa embebido de Google Maps
3. Click en "Ver en Google Maps" para abrir en una nueva pestaña

---

## 🖼️ Si la Imagen del Edificio No Aparece

### Solución Temporal
Si no has guardado la imagen aún, verás un icono de imagen rota. Para solucionarlo:

1. **Opción 1**: Ejecuta `python copiar_imagen_edificio.py`
2. **Opción 2**: Guarda manualmente la imagen en:
   ```
   d:\ESCRITORIO\InmobiliariaApp\properties\static\img\edificio-isma.jpg
   ```
3. **Opción 3**: Usa una imagen temporal mientras consigues la oficial

### Usar Imagen Temporal (Opcional)
Si necesitas una imagen temporal, puedes usar una de internet:
```html
<!-- En home.html, reemplaza temporalmente: -->
<img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab" ...>
```

---

## 🐛 Solución de Problemas Comunes

### La página no carga
```bash
# Asegúrate de estar en la carpeta correcta
cd d:\ESCRITORIO\InmobiliariaApp

# Verifica que el servidor esté corriendo
python manage.py runserver
```

### Los estilos no se ven
```bash
# Recopila archivos estáticos
python manage.py collectstatic --noinput
```

### Error 404 en imágenes
```bash
# Verifica que las imágenes existan en:
dir properties\static\img
```

---

## 📊 Métricas de Mejora

### Antes vs Después

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Ubicación** | Genérica (Medellín) | Específica (Edificio ISMA, Bello) |
| **Contacto** | Un solo número | Múltiples canales + WhatsApp |
| **Asesor** | No destacado | Andrés Villegas prominente |
| **Diseño** | Básico | Moderno con glassmorphism |
| **Secciones** | 5 | 7 (incluyendo oficina) |
| **Mapa** | No había | Google Maps integrado |
| **WhatsApp** | No había | Botones directos |

---

## 🎉 ¡Listo para Producción!

Una vez que hayas verificado todo, tu sitio está listo para:

1. ✅ Mostrar a clientes
2. ✅ Compartir en redes sociales
3. ✅ Usar en campañas de marketing
4. ✅ Recibir consultas de clientes

---

## 📞 Información de Contacto en el Sitio

**Inmobiliaria**: Empresa G&D Inmobiliario  
**Ubicación**: CRA 50 # 37-13, Oficina 609  
**Edificio**: Edificio Empresarial ISMA  
**Ciudad**: Bello, Colombia  
**Teléfono**: +57 301 342 1846  
**Email**: grupo.bienes.raices.j.h@gmail.com  
**Asesor**: Andrés Villegas  
**Horario**: Lun-Vie 8am-6pm, Sáb 9am-1pm  

---

## 🔗 Links Útiles

- **Servidor local**: http://localhost:8000
- **Admin panel**: http://localhost:8000/admin
- **Ver propiedades**: http://localhost:8000/properties
- **Contacto**: http://localhost:8000/contact

---

**¡Disfruta tu sitio actualizado! 🚀**

Si tienes alguna pregunta o necesitas ajustes adicionales, no dudes en consultar.
