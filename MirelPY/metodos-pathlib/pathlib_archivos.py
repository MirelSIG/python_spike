# Demo de pathlib para operaciones comunes con archivos
from pathlib import Path

print("=== PATHLIB: ARCHIVOS DEL DIA A DIA ===")

base = Path(".").resolve()
workspace = base / "MirelPY" / "metodos-pathlib"
demo_dir = workspace / "demo_workspace"
demo_file = demo_dir / "notas_dev.txt"

# 1) Crear carpeta si no existe
print("1) Crear carpeta demo")
demo_dir.mkdir(parents=True, exist_ok=True)
print(f"Carpeta lista: {demo_dir.exists()} -> {demo_dir}")

# 2) Escribir texto
print("\n2) Escribir archivo")
demo_file.write_text("TODO:\n- Revisar logs\n- Actualizar README\n", encoding="utf-8")
print(f"Archivo creado: {demo_file.exists()} -> {demo_file.name}")

# 3) Leer texto
print("\n3) Leer archivo")
contenido = demo_file.read_text(encoding="utf-8")
print(contenido)

# 4) Renombrar archivo
print("4) Renombrar archivo")
renombrado = demo_dir / "tareas_dev.txt"
demo_file.rename(renombrado)
print(f"Renombrado: {renombrado.exists()} -> {renombrado.name}")

# 5) Limpieza opcional de la demo
print("\n5) Limpieza")
renombrado.unlink(missing_ok=True)
print("Archivo eliminado.")
