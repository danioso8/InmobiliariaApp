#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Colectar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones
python manage.py migrate

# Crear superusuario si no existe
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@inmobiliaria.com', 'admin123')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
END
