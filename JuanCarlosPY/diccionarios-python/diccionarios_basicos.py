# Ejemplos de métodos de Diccionarios en Python
# Los diccionarios almacenan pares clave-valor

print("=== MÉTODOS BÁSICOS ===")
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(f"Diccionario: {persona}")
print(f"len(): {len(persona)}")

print("\n=== MÉTODOS keys(), values(), items() ===")
libro = {"titulo": "Python Avanzado", "autor": "Dev Expert", "año": 2023, "precio": 29.99}
print(f"Diccionario: {libro}")
print(f"keys(): {list(libro.keys())}")
print(f"values(): {list(libro.values())}")
print(f"items(): {list(libro.items())}")

print("\n=== MÉTODO get() - Acceso Seguro ===")
config = {"host": "localhost", "port": 8080, "debug": True}
print(f"Diccionario: {config}")
print(f"get('host'): {config.get('host')}")
print(f"get('timeout'): {config.get('timeout')}")
print(f"get('timeout', 30): {config.get('timeout', 30)}")

print("\n=== MÉTODOS update() y pop() ===")
inventario = {"manzanas": 10, "naranjas": 5}
print(f"Original: {inventario}")
inventario.update({"peras": 8, "uvas": 15})
print(f"Después de update(): {inventario}")
valor = inventario.pop("naranjas")
print(f"Después de pop('naranjas'): {inventario}")
print(f"Valor extraído: {valor}")

print("\n=== MÉTODO setdefault() ===")
contador = {"a": 5, "b": 3}
print(f"Diccionario: {contador}")
print(f"setdefault('a', 0): {contador.setdefault('a', 0)}")
print(f"setdefault('c', 0): {contador.setdefault('c', 0)}")
print(f"Diccionario después: {contador}")

print("\n=== ACCESO Y MODIFICACIÓN ===")
producto = {"nombre": "Laptop", "precio": 999, "stock": 5}
print(f"Original: {producto}")
producto["precio"] = 899
producto["descuento"] = "10%"
print(f"Modificado: {producto}")

print("\n=== ITERACIÓN ===")
frutas = {"manzana": 2.5, "banana": 1.8, "naranja": 3.0}
print(f"Precios de frutas:")
for fruta, precio in frutas.items():
    print(f"  {fruta}: ${precio}")
