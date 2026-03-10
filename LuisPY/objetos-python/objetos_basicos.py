class Robot:
    # Atributo de clase (para el Administrador/Classmethod)
    total_robots = 0

    # 1. EL PREPARADOR (init)
    def __init__(self, nombre, version):
        self.nombre = nombre    # Atributo de instancia
        self.version = version  # Atributo de instancia
        Robot.total_robots += 1

    # 2. EL LENTE (str) - Para que print() funcione bonito
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