"""
Script para copiar la imagen del Edificio ISMA desde la carpeta de Descargas
Autor: Empresa G&D Inmobiliario
Fecha: Diciembre 2025
"""

import os
import shutil
from pathlib import Path

def copiar_imagen_edificio():
    """
    Busca y copia la imagen del edificio ISMA desde diferentes ubicaciones comunes
    """
    # Ruta de destino
    destino = Path(r"d:\ESCRITORIO\InmobiliariaApp\properties\static\img\edificio-isma.jpg")
    
    # Posibles ubicaciones de la imagen
    posibles_rutas = [
        Path.home() / "Downloads" / "edificio-isma.jpg",
        Path.home() / "Downloads" / "edificio.jpg",
        Path.home() / "Descargas" / "edificio-isma.jpg",
        Path.home() / "Descargas" / "edificio.jpg",
        Path.home() / "Desktop" / "edificio-isma.jpg",
        Path.home() / "Desktop" / "edificio.jpg",
        Path.home() / "Escritorio" / "edificio-isma.jpg",
        Path.home() / "Escritorio" / "edificio.jpg",
    ]
    
    # Buscar la imagen en las posibles ubicaciones
    imagen_encontrada = None
    for ruta in posibles_rutas:
        if ruta.exists():
            imagen_encontrada = ruta
            print(f"✅ Imagen encontrada en: {ruta}")
            break
    
    if imagen_encontrada:
        try:
            # Copiar la imagen
            shutil.copy2(imagen_encontrada, destino)
            print(f"✅ Imagen copiada exitosamente a: {destino}")
            print("\n🎉 ¡Listo! La imagen del Edificio ISMA está ahora en la aplicación.")
            print("Puedes ver el resultado ejecutando el servidor de desarrollo.")
            return True
        except Exception as e:
            print(f"❌ Error al copiar la imagen: {e}")
            return False
    else:
        print("❌ No se encontró la imagen en las ubicaciones comunes.")
        print("\n📝 Por favor:")
        print("1. Descarga la imagen del edificio que adjuntaste en el chat")
        print("2. Renómbrala como 'edificio-isma.jpg'")
        print("3. Guárdala en tu carpeta de Descargas")
        print("4. Ejecuta este script nuevamente")
        print(f"\nO cópiala manualmente a: {destino}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("📸 Instalador de Imagen - Edificio Empresarial ISMA")
    print("   Bienes Raíces JH")
    print("=" * 60)
    print()
    
    copiar_imagen_edificio()
    
    print()
    print("=" * 60)
    input("Presiona Enter para salir...")
