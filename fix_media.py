#!/usr/bin/env python
"""Script para mover imágenes de banners/ a media/banners/"""

import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Crear directorio media/banners
media_banners = BASE_DIR / 'media' / 'banners'
media_banners.mkdir(parents=True, exist_ok=True)
print(f"✓ Carpeta creada: {media_banners}")

# Mover archivos de banners/ a media/banners/
banners_dir = BASE_DIR / 'banners'
if banners_dir.exists():
    for file in banners_dir.iterdir():
        if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            dst = media_banners / file.name
            shutil.copy2(file, dst)
            print(f"✓ Copiado: {file.name}")

# Mostrar estructura
print("\n=== ESTRUCTURA CREADA ===")
for root, dirs, files in os.walk(BASE_DIR / 'media'):
    level = str(root).replace(str(BASE_DIR / 'media'), '').count(os.sep)
    indent = '  ' * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = '  ' * (level + 1)
    for file in files:
        print(f'{subindent}{file}')

print("\n✓ ¡Estructura de media creada exitosamente!")
print("\nAhora:")
print("1. Reinicia el servidor Django")
print("2. Las imágenes deberían aparecer en el carrusel")
