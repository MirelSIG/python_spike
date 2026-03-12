class Robot:
    # Atributo de clase (para el Administrador/Classmethod)
    total_robots = 0

    # 1. EL PREPARADOR (init)
    def __init__(self, nombre, version):
        self.nombre = nombre    
        self.version = version  
        Robot.total_robots += 1

    # 2. Para que print() funcione 
    def __str__(self):
        return f" Robot: {self.nombre} (v{self.version})"

    # 3. MÉTODO NORMAL (instancia) - Acciones del objeto
    def saludar(self):
        print(f"Hola, soy {self.nombre}. ¿En qué puedo ayudarte?")

    # 4. EL ADMINISTRADOR (classmethod) - Gestiona la "fábrica"
    @classmethod
    def cuantas_unidades(cls):
        print(f"Se han fabricado {cls.total_robots} robots en total.")

    # 5. LA HERRAMIENTA (staticmethod) - Utilidad independiente
    @staticmethod
    def es_nombre_valido(nombre):
        return len(nombre) > 2

# --- PRUEBA DE TODO ---
bot1 = Robot("R2D2", 1.0)
bot2 = Robot("C3PO", 2.1)

print(bot1)                # <--- Aquí usas el "LENTE" (__str__)
bot1.saludar()             # <--- Método NORMAL
Robot.cuantas_unidades()   # <--- Método de CLASE (el administrador)

robot = {"nombre": "R2-D2", "version": 1.2}



#-------------------------------------------------------------

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 25)

#-------------------------------------------------------------

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

        def __str__(self):
            return f"Persona llamada {self.nombre}"

p = Persona("Ana")
print(p)

#-------------------------------------------------------------

class Coche:
    def arrancar(self):
        print("El coche está arrancando")

mi_coche = Coche()
mi_coche.arrancar()


#-------------------------------------------------------------
class Persona:
    especie = "Humano"

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def crear_sin_nombre(cls):
        return cls("Desconocido")

p = Persona.crear_sin_nombre()
#-------------------------------------------------------------

class Matematica:

    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Matematica.sumar(5, 3)
print(resultado)