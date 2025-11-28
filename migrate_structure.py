import os
import shutil

print("🏠 Iniciando migración automática de CompuEasys a InmobiliariaApp...")
print("=" * 60)

# Rutas
source_project = r"D:\ESCRITORIO\CompueasysApp"
target_project = r"D:\ESCRITORIO\InmobiliariaApp"

# Crear directorios necesarios
dirs_to_create = [
    "properties/templates/properties",
    "properties/static/css",
    "properties/static/js", 
    "properties/static/img",
    "admin_panel/templates/admin_panel",
    "admin_panel/static/css",
    "admin_panel/static/js",
    "media_files/properties",
    "staticfiles"
]

for dir_path in dirs_to_create:
    full_path = os.path.join(target_project, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"✅ Creado: {dir_path}")

print("\n📁 Estructura de directorios creada exitosamente!")
print("=" * 60)
