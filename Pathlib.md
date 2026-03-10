
**¿Por qué la librería Pathlib?**

Durante muchos años, Python manejó rutas de archivos usando **cadenas de
texto** y funciones sueltas del módulo os y os.path. Esto generaba
varios problemas:

-   Las rutas eran *strings*, no objetos → difícil de manipular.

-   Había que preocuparse por las diferencias entre sistemas:

    -   Windows: C:\\Users\\Mirel\\Documents

    -   Linux/Mac: /home/mirel/Documents

-   Muchas operaciones eran verbosas:

  -----------------------------------------------------------------------
  os.path.join(os.path.dirname(path), \"archivo.txt\")

  -----------------------------------------------------------------------

Para resolver esto, Python introdujo pathlib (desde Python 3.4), un
módulo que convierte las rutas en **objetos inteligentes**, fáciles de
combinar, manipular y usar.

# Concepto fundamental: *una ruta como un objeto*

pathlib introduce la clase Path, que representa una ruta como un objeto
con métodos y propiedades.

+-----------------------------------------------------------------------+
| from pathlib import Path                                              |
|                                                                       |
| ruta = Path(\"carpeta/archivo.txt\")                                  |
+-----------------------------------------------------------------------+

Este objeto:

-   Sabe si existe

-   Sabe si es archivo o carpeta

-   Permite navegar por el sistema de archivos

-   Permite leer y escribir archivos

-   Se comporta igual en Windows, Linux y Mac

# Uso básico: lo esencial para empezar

## 📌 Crear rutas

+-----------------------------------------------------------------------+
| from pathlib import Path                                              |
|                                                                       |
| p = Path(\"carpeta\") / \"subcarpeta\" / \"archivo.txt\"              |
+-----------------------------------------------------------------------+

El operador / se sobrecarga para unir rutas → mucho más legible.

## 📌 Comprobar existencia

+-----------------------------------------------------------------------+
| p.exists()                                                            |
|                                                                       |
| p.is_file()                                                           |
|                                                                       |
| p.is_dir()                                                            |
+-----------------------------------------------------------------------+

📌 Crear carpetas

  -----------------------------------------------------------------------
  Path(\"nueva/carpeta\").mkdir(parents=True, exist_ok=True)

  -----------------------------------------------------------------------

📌 Leer un archivo

  -----------------------------------------------------------------------
  contenido = Path(\"notas.txt\").read_text()

  -----------------------------------------------------------------------

📌 Escribir un archivo

  -----------------------------------------------------------------------
  Path(\"salida.txt\").write_text(\"Hola, mundo\")

  -----------------------------------------------------------------------

# Nivel intermedio: navegar y manipular rutas

## 📂 Listar archivos de un directorio

+-----------------------------------------------------------------------+
| for archivo in Path(\"carpeta\").iterdir():                           |
|                                                                       |
| print(archivo)                                                        |
+-----------------------------------------------------------------------+

🔍 **Buscar archivos por patrón**

+-----------------------------------------------------------------------+
| for txt in Path(\".\").glob(\"\*.txt\"):                              |
|                                                                       |
| print(txt)                                                            |
+-----------------------------------------------------------------------+

**🧩 Obtener partes de la ruta**

+-----------------------------------------------------------------------+
| p = Path(\"/home/mirel/proyecto/main.py\")                            |
|                                                                       |
| p.name \# \'main.py\'                                                 |
|                                                                       |
| p.stem \# \'main\'                                                    |
|                                                                       |
| p.suffix \# \'.py\'                                                   |
|                                                                       |
| p.parent \# \'/home/mirel/proyecto\'                                  |
|                                                                       |
| p.parts \# (\'/\', \'home\', \'mirel\', \'proyecto\', \'main.py\')    |
+-----------------------------------------------------------------------+

#  

# **🚀 Nivel avanzado: operaciones complejas y buenas prácticas**

## 🧪 Trabajar con rutas absolutas y relativas

+-----------------------------------------------------------------------+
| p.resolve() \# Convierte a ruta absoluta real                         |
|                                                                       |
| p.relative_to(\"/home/mirel\")                                        |
+-----------------------------------------------------------------------+

**🧹 Eliminar archivos y carpetas**

+-----------------------------------------------------------------------+
| Path(\"archivo.txt\").unlink() \# borrar archivo                      |
|                                                                       |
| Path(\"carpeta\").rmdir() \# borrar carpeta vacía                     |
+-----------------------------------------------------------------------+

**🧵 Lectura y escritura binaria**

+-----------------------------------------------------------------------+
| data = Path(\"imagen.png\").read_bytes()                              |
|                                                                       |
| Path(\"copia.png\").write_bytes(data)                                 |
+-----------------------------------------------------------------------+

**🧱 Integración con otras librerías**

**Muchísimas librerías modernas aceptan objetos Path directamente:**

-   pandas.read_csv(Path(\"datos.csv\"))

-   open(Path(\"archivo.txt\"))

-   shutil.copy(Path(\"a\"), Path(\"b\"))

# **🎯 ¿Por qué pathlib es tan útil?**

## Ventajas clave

  -----------------------------------------------------------------------
  Ventaja               Explicación
  --------------------- -------------------------------------------------
  **Portabilidad**      Funciona igual en Windows, Linux y Mac

  **Legibilidad**       El código es más claro y expresivo

  **Orientado a         Las rutas tienen métodos útiles
  objetos**             

  **Menos errores**     Evita problemas con barras, escapes y
                        concatenaciones

  **Integración         Muchas librerías ya lo usan como estándar
  moderna**             
  -----------------------------------------------------------------------

# **🎯 ¿Por qué pathlib es tan útil?**

## Ventajas clave

  -----------------------------------------------------------------------
  Ventaja               Explicación
  --------------------- -------------------------------------------------
  **Portabilidad**      Funciona igual en Windows, Linux y Mac

  **Legibilidad**       El código es más claro y expresivo

  **Orientado a         Las rutas tienen métodos útiles
  objetos**             

  **Menos errores**     Evita problemas con barras, escapes y
                        concatenaciones

  **Integración         Muchas librerías ya lo usan como estándar
  moderna**             
  -----------------------------------------------------------------------

# **🌟 Conclusión**

pathlib es una de esas librerías que **cambian tu forma de programar**
en Python:

-   Te quita problemas de encima

-   Hace tu código más limpio

-   Te prepara para proyectos profesionales

-   Es el estándar moderno para trabajar con archivos

Si estás empezando, dominar pathlib te da una base sólida para cualquier
proyecto que toque el sistema de archivos.

# **🧭 Comparación general: pathlib vs os.path**

  ----------------------------------------------------------------------------
  Aspecto              pathlib                      os.path
  -------------------- ---------------------------- --------------------------
  **Paradigma**        Orientado a objetos          Funciones procedimentales

  **Tipo de dato**     Objetos Path                 Cadenas de texto (str)

  **Legibilidad**      Muy alta                     Media

  **Portabilidad**     Automática                   Manual (hay que tener
                       (Windows/Linux/Mac)          cuidado)

  **Operaciones**      Métodos intuitivos           Funciones sueltas
                       (.read_text(), .exists())    (os.path.exists())

  **Concatenación de   Operador /                   os.path.join()
  rutas**                                           

  **Moderno?**         Sí, recomendado              Antiguo, legado

  **Compatibilidad**   Excelente con librerías      Aún funciona, pero menos
                       modernas                     elegante
  ----------------------------------------------------------------------------

# 🌱 1. Filosofía: ¿por qué existen dos módulos?

## os.path

-   Es la forma **histórica** de trabajar con rutas en Python.

-   Basado en **strings** y funciones.

-   Funciona, pero es más verboso y propenso a errores.

## pathlib

-   Introducido en Python 3.4 para **modernizar** el manejo de rutas.

-   Convierte las rutas en **objetos inteligentes**.

-   Reduce errores y hace el código más legible.

# 🧱 2. Diferencia clave: *string vs objeto*

## 🔹 os.path → rutas como texto

+-----------------------------------------------------------------------+
| import os                                                             |
|                                                                       |
| ruta = \"carpeta/archivo.txt\"                                        |
|                                                                       |
| os.path.exists(ruta)                                                  |
+-----------------------------------------------------------------------+

**🔹 pathlib → rutas como objetos**

+-----------------------------------------------------------------------+
| from pathlib import Path                                              |
|                                                                       |
| ruta = Path(\"carpeta\") / \"archivo.txt\"                            |
|                                                                       |
| ruta.exists()                                                         |
+-----------------------------------------------------------------------+

Esto cambia completamente la experiencia: con pathlib las rutas tienen
métodos, propiedades y comportamiento propio.

## **3. Concatenación de rutas**

## Con os.path

  -----------------------------------------------------------------------
  ruta = os.path.join(\"carpeta\", \"subcarpeta\", \"archivo.txt\")

  -----------------------------------------------------------------------

## **Con** pathlib

  -----------------------------------------------------------------------
  ruta = Path(\"carpeta\") / \"subcarpeta\" / \"archivo.txt\"

  -----------------------------------------------------------------------

El operador / es mucho más natural y evita errores.

# 📂 4. Lectura y escritura de archivos

## Con os.path + open()

+-----------------------------------------------------------------------+
| with open(\"archivo.txt\", \"r\") as f:                               |
|                                                                       |
| contenido = f.read()                                                  |
+-----------------------------------------------------------------------+

**Con** pathlib

  -----------------------------------------------------------------------
  contenido = Path(\"archivo.txt\").read_text()

  -----------------------------------------------------------------------

Y para escribir:

  -----------------------------------------------------------------------
  Path(\"salida.txt\").write_text(\"Hola\")

  -----------------------------------------------------------------------

# 🔍 **5. Obtener partes de la ruta**

## Con os.path

+-----------------------------------------------------------------------+
| os.path.basename(ruta)                                                |
|                                                                       |
| os.path.dirname(ruta)                                                 |
|                                                                       |
| os.path.splitext(ruta)                                                |
+-----------------------------------------------------------------------+

**Con** pathlib

+-----------------------------------------------------------------------+
| p = Path(\"carpeta/archivo.txt\")                                     |
|                                                                       |
| p.name \# \'archivo.txt\'                                             |
|                                                                       |
| p.stem \# \'archivo\'                                                 |
|                                                                       |
| p.suffix \# \'.txt\'                                                  |
|                                                                       |
| p.parent \# \'carpeta\'                                               |
+-----------------------------------------------------------------------+

Mucho más expresivo.

# 6. Portabilidad entre sistemas operativos

## os.path

Debes preocuparte por:

-   barras invertidas \\ en Windows

-   barras / en Linux/Mac

-   encoding

-   normalización

## pathlib

Lo hace automáticamente:

-   En Windows usa WindowsPath

-   En Linux/Mac usa PosixPath

Tu código es **universal** sin esfuerzo.

# 🚀 7. Búsqueda de archivos

## Con os.listdir() y filtros manuales

+-----------------------------------------------------------------------+
| for archivo in os.listdir(\".\"):                                     |
|                                                                       |
| if archivo.endswith(\".txt\"):                                        |
|                                                                       |
| print(archivo)                                                        |
+-----------------------------------------------------------------------+

**Con** pathlib.glob()

+-----------------------------------------------------------------------+
| for archivo in Path(\".\").glob(\"\*.txt\"):                          |
|                                                                       |
| print(archivo)                                                        |
+-----------------------------------------------------------------------+

# 🧹 **8. Crear y borrar archivos/carpetas**

## os.path + os + shutil

+-----------------------------------------------------------------------+
| os.mkdir(\"carpeta\")                                                 |
|                                                                       |
| os.remove(\"archivo.txt\")                                            |
+-----------------------------------------------------------------------+

Pathlib

+-----------------------------------------------------------------------+
| Path(\"carpeta\").mkdir()                                             |
|                                                                       |
| Path(\"archivo.txt\").unlink()                                        |
+-----------------------------------------------------------------------+

# 9. Integración con librerías modernas

Hoy en día, muchas librerías aceptan directamente objetos Path:

-   pandas

-   matplotlib

-   shutil

-   open()

-   json, csv, etc.

Ejemplo:

+-----------------------------------------------------------------------+
| import pandas as pd                                                   |
|                                                                       |
| df = pd.read_csv(Path(\"datos.csv\"))                                 |
+-----------------------------------------------------------------------+

Con os.path tendrías que pasar strings.

­\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# 🎯 10. ¿Cuándo usar cada uno?

## Usa pathlib cuando:

-   Empiezas un proyecto nuevo

-   Quieres código limpio y moderno

-   Trabajas con muchas rutas

-   Necesitas portabilidad

-   Quieres evitar errores con barras y concatenaciones

## Usa os.path cuando:

-   Mantienes código antiguo

-   Una librería antigua solo acepta strings (cada vez menos común)

# 🏆 Conclusión

pathlib no es solo una alternativa: **es la evolución natural y moderna
del manejo de rutas en Python.**

Te ofrece:

-   Más legibilidad

-   Menos errores

-   Código más corto

-   Portabilidad automática

-   Métodos integrados para leer, escribir y manipular archivos

os.path sigue siendo útil, pero pertenece a una era anterior del
lenguaje.
