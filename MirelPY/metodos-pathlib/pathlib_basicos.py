# Demo sencilla de pathlib
# pathlib permite trabajar con rutas de forma clara y multiplataforma.

from pathlib import Path

print("=== DEMO BÁSICA DE PATHLIB ===")

# Ruta base del proyecto (directorio actual donde se ejecuta el script)
base = Path(".").resolve()
print(f"Directorio actual: {base}")

# Construir rutas con el operador /
archivo_demo = base / "MirelPY" / "metodos-strings" / "strings_basicos.py"
print(f"Ruta construida: {archivo_demo}")

# Consultar propiedades comunes
print(f"¿Existe?: {archivo_demo.exists()}")
print(f"¿Es archivo?: {archivo_demo.is_file()}")
print(f"Nombre: {archivo_demo.name}")
print(f"Extensión: {archivo_demo.suffix}")

# Listar algunos archivos Python dentro de MirelPY
carpeta_mirel = base / "MirelPY"
print("\nArchivos .py en MirelPY (primeros 5):")
for i, ruta in enumerate(carpeta_mirel.rglob("*.py"), start=1):
    print(f"{i}. {ruta.relative_to(base)}")
    if i >= 5:
        break
