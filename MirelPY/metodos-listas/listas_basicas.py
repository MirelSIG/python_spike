# Ejemplos de métodos de Listas en Python
# Las listas son MUTABLES - muchos métodos modifican la lista original

print("=== MÉTODOS DE AGREGAR ELEMENTOS ===")
numeros = [1, 2, 3]
print(f"Lista original: {numeros}")
numeros.append(4)
print(f"Después de append(4): {numeros}")
numeros.extend([5, 6])
print(f"Después de extend([5,6]): {numeros}")
numeros.insert(0, 0)
print(f"Después de insert(0, 0): {numeros}")

print("\n=== MÉTODOS DE ELIMINAR ELEMENTOS ===")
colores = ["rojo", "azul", "verde", "amarillo", "azul"]
print(f"Lista original: {colores}")
colores.remove("azul")
print(f"Después de remove('azul'): {colores}")
ultimo = colores.pop()
print(f"Después de pop(): {colores} | Elemento extraído: {ultimo}")

print("\n=== MÉTODOS DE ORDENAMIENTO ===")
valores = [5, 2, 8, 1, 9]
print(f"Lista original: {valores}")
valores.sort()
print(f"Después de sort(): {valores}")
valores.reverse()
print(f"Después de reverse(): {valores}")

print("\n=== MÉTODOS DE BÚSQUEDA ===")
letras = ["a", "b", "c", "b", "d"]
print(f"Lista: {letras}")
print(f"count('b'): {letras.count('b')}")
print(f"len(): {len(letras)}")

print("\n=== SLICING ===")
serie = [10, 20, 30, 40, 50]
print(f"Lista: {serie}")
print(f"[1:4]: {serie[1:4]}")
print(f"[::-1] (invertir): {serie[::-1]}")
