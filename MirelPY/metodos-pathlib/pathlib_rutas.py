# Demo de pathlib para navegacion de rutas
from pathlib import Path

print("=== PATHLIB: RUTAS DEL PROYECTO ===")

base = Path(".").resolve()
print(f"Proyecto actual: {base}")
print(f"Carpeta padre: {base.parent}")
print(f"Partes de la ruta: {base.parts}")

ruta_src = base / "MirelPY" / "metodos-strings" / "strings_basicos.py"
print("\nRuta construida con '/':")
print(ruta_src)

print("\nPropiedades utiles:")
print(f"name: {ruta_src.name}")
print(f"stem: {ruta_src.stem}")
print(f"suffix: {ruta_src.suffix}")
print(f"suffixes: {ruta_src.suffixes}")
print(f"exists: {ruta_src.exists()}")

if ruta_src.exists():
    print(f"relative_to(base): {ruta_src.relative_to(base)}")
