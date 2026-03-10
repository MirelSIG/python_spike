# Ejemplos de métodos de Strings en Python
# Los strings son INMUTABLES - todos los métodos devuelven un nuevo string

print("=== MÉTODOS DE TRANSFORMACIÓN ===")
texto = "python es genial"
print(f"Original: {texto}")
print(f"upper(): {texto.upper()}")
print(f"capitalize(): {texto.capitalize()}")
print(f"title(): {texto.title()}")

print("\n=== MÉTODOS DE BÚSQUEDA ===")
frase = "banana split con banana"
print(f"Texto: {frase}")
print(f"find('banana'): {frase.find('banana')}")
print(f"count('banana'): {frase.count('banana')}")
print(f"count('a'): {frase.count('a')}")

print("\n=== MÉTODOS DE DIVISIÓN Y UNIÓN ===")
csv = "manzana,naranja,pera,uva"
print(f"CSV original: {csv}")
frutas = csv.split(',')
print(f"split(','): {frutas}")
print(f"join() con ' | ': {' | '.join(frutas)}")

print("\n=== SLICING (OPERACIÓN) ===")
palabra = "Programación"
print(f"Palabra: {palabra}")
print(f"[0:5]: {palabra[0:5]}")
print(f"[::-1] (invertir): {palabra[::-1]}")
