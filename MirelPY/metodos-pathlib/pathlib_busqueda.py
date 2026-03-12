# Demo de pathlib para busqueda de archivos (glob/rglob)
from pathlib import Path

print("=== PATHLIB: BUSQUEDA DE ARCHIVOS ===")

base = Path(".").resolve()
carpeta = base / "MirelPY"

print(f"Buscando en: {carpeta}")
print("\nArchivos Python con glob('*.py') en la raiz de MirelPY:")
for ruta in carpeta.glob("*.py"):
    print(f"- {ruta.relative_to(base)}")

print("\nPrimeros 10 archivos Python con rglob('*.py') recursivo:")
for i, ruta in enumerate(carpeta.rglob("*.py"), start=1):
    print(f"{i}. {ruta.relative_to(base)}")
    if i >= 10:
        break

print("\nFiltrado por nombre que contiene 'basicos':")
for ruta in carpeta.rglob("*basicos*.py"):
    print(f"- {ruta.relative_to(base)}")
