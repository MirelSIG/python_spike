# Ejemplos de Objetos en Python
# Objetos y programación orientada a objetos

print("=== CLASES Y OBJETOS ===")
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def describir(self):
        return f"{self.marca} {self.modelo} ({self.año})"

auto = Vehiculo("Toyota", "Corolla", 2020)
print(f"Objeto creado: {auto.describir()}")
print(f"Marca: {auto.marca}")
print(f"Modelo: {auto.modelo}")
print(f"Año: {auto.año}")

print("\n=== MÉTODO len() EN OBJETOS ===")
# len() funciona con cualquier objeto que implemente __len__
class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar(self, producto):
        self.productos.append(producto)
    
    def __len__(self):
        return len(self.productos)

inventario = Inventario()
inventario.agregar("Laptop")
inventario.agregar("Mouse")
inventario.agregar("Teclado")
print(f"Productos en inventario: {len(inventario)}")

print("\n=== ATRIBUTOS Y MÉTODOS ===")
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado
    
    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

calc = Calculadora()
print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"4 * 7 = {calc.multiplicar(4, 7)}")
print(f"Último resultado: {calc.resultado}")

print("\n=== HERENCIA ===")
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

perro = Perro("Max")
gato = Gato("Luna")
print(f"{perro.nombre} dice: {perro.hacer_sonido()}")
print(f"{gato.nombre} dice: {gato.hacer_sonido()}")
