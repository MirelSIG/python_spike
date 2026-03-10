# 🐍 Python Spike — Grupo 3

> **Bootcamp Desarrollo Web Fullstack · Peñascal – Somos F5**

---

## 📌 Descripción

Este repositorio es un **fork** del proyecto original [python_investigacion](https://github.com/alvarezmarlen/python_investigacion) y ha sido adaptado como **Spike de investigación** por el **Grupo 3** del Bootcamp de Desarrollo Web Fullstack de **Peñascal – Somos F5**.

Un _Spike_ es una tarea de investigación técnica acotada cuyo objetivo es explorar un tema desconocido, reducir incertidumbre y compartir el conocimiento adquirido con el equipo. En este caso el tema asignado es:

> **Manipulación de tipos de datos en Python: Strings, Listas, Diccionarios y Objetos (POO)**

El resultado es una **aplicación web interactiva** que permite visualizar y ejecutar código Python directamente en el navegador, sin necesidad de instalar ningún entorno local, gracias a [Pyodide](https://pyodide.org/).

---

## 👥 Integrantes y temáticas

| Integrante | Tema | Carpeta |
|---|---|---|
| **Mirel** | Strings y Listas | `MirelPY/` |
| **Luis** | Objetos (Programación Orientada a Objetos) | `LuisPY/` |
| **Juan Carlos** | Diccionarios | `JuanCarlosPY/` |

---

## 🎯 Objetivos del Spike

1. Investigar y documentar con ejemplos ejecutables los principales **tipos de datos** de Python.
2. Comprender la diferencia entre tipos **mutables** (listas, diccionarios) e **inmutables** (strings).
3. Introducir los fundamentos de la **Programación Orientada a Objetos** (clases, herencia, métodos especiales).
4. Presentar los hallazgos al resto del bootcamp a través de una interfaz web visual e interactiva.

---

## 🗂️ Estructura del proyecto

```
python_spike/
│
├── index.html                          # Landing page — punto de entrada
│
├── Navbar/
│   ├── index.css                       # Estilos compartidos del navbar
│   └── index.html                      # Componente navbar (referencia)
│
├── MirelPY/                            # Sección de Mirel
│   ├── index.html
│   ├── index.css
│   ├── terminal.js                     # Lógica de terminal interactiva
│   ├── metodos-strings/
│   │   └── strings_basicos.py          # Ejemplos: upper, find, split, slicing…
│   └── metodos-listas/
│       └── listas_basicas.py           # Ejemplos: append, sort, pop, slicing…
│
├── LuisPY/                             # Sección de Luis
│   ├── index.html
│   ├── index.css
│   ├── terminal.js
│   └── objetos-python/
│       └── objetos_basicos.py          # Ejemplos: clases, herencia, __len__…
│
├── JuanCarlosPY/                       # Sección de Juan Carlos
│   ├── index.html
│   ├── index.css
│   ├── terminal.js
│   └── diccionarios-python/
│       └── diccionarios_basicos.py     # Ejemplos: get, update, pop, setdefault…
│
└── sintaxis_framework/
    └── sintaxis.py                     # Referencia de sintaxis general de Python
```

---

## 🧪 Contenido investigado

### 📝 Strings (Mirel)
Los strings son **inmutables**: ningún método modifica el original, siempre se devuelve uno nuevo.

| Categoría | Métodos cubiertos |
|---|---|
| Transformación | `upper()`, `lower()`, `capitalize()`, `title()` |
| Búsqueda | `find()`, `count()` |
| División y unión | `split()`, `join()` |
| Slicing | `[inicio:fin]`, `[::-1]` |

---

### 📋 Listas (Mirel)
Las listas son **mutables**: sus métodos modifican la estructura original.

| Categoría | Métodos cubiertos |
|---|---|
| Agregar elementos | `append()`, `extend()`, `insert()` |
| Eliminar elementos | `remove()`, `pop()` |
| Ordenamiento | `sort()`, `reverse()` |
| Búsqueda / info | `count()`, `len()` |
| Slicing | `[inicio:fin]`, `[::-1]` |

---

### 🧩 Objetos — POO (Luis)
Introducción a la **Programación Orientada a Objetos** en Python.

| Concepto | Descripción |
|---|---|
| Clases y objetos | Definición con `class`, instanciación, `__init__` |
| Atributos | Atributos de instancia (`self.*`) |
| Métodos | Métodos de instancia, valor de retorno |
| Métodos especiales | `__len__`, `__str__` |
| Herencia | Clase base → clase derivada, `super()` |

---

### 📚 Diccionarios (Juan Carlos)
Colecciones de pares **clave-valor**, mutables y sin orden garantizado en versiones antiguas (ordenados por inserción desde Python 3.7).

| Categoría | Métodos cubiertos |
|---|---|
| Consulta | `keys()`, `values()`, `items()`, `get()`, `len()` |
| Modificación | `update()`, `pop()`, `setdefault()` |
| Acceso directo | `dict[clave]`, asignación de nuevas claves |
| Iteración | `for clave, valor in dict.items()` |

---

## 🚀 Cómo ejecutar el proyecto

Al ser una aplicación web estática, los archivos `.py` se cargan mediante `fetch()` por lo que es necesario un servidor HTTP local:

```bash
# Opción 1 — Python (recomendado)
cd python_spike
python3 -m http.server 8000
# → Abrir http://localhost:8000

# Opción 2 — Node.js (npx)
npx serve .
```

> ⚠️ **No abrir los archivos directamente con `file://`** — el `fetch()` hacia los `.py` bloqueará por política CORS del navegador.

---

## ⚙️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **HTML5 / CSS3** | Estructura y estilos de la interfaz |
| **JavaScript (ES2022)** | Lógica de la terminal interactiva |
| **[Pyodide v0.25](https://pyodide.org/)** | Ejecución de Python en el navegador (WebAssembly) |
| **Google Fonts — Inter** | Tipografía |
| **Git / GitHub** | Control de versiones y colaboración |

---

## 🔀 Fork y procedimiento de trabajo

1. **Fork** del repositorio [`alvarezmarlen/python_investigacion`](https://github.com/alvarezmarlen/python_investigacion) como base de la estructura.
2. Cada integrante desarrolló su sección en su carpeta correspondiente (`MirelPY/`, `LuisPY/`, `JuanCarlosPY/`).
3. Se creó la **landing page** (`index.html`) como punto de entrada unificado.
4. El código Python de cada sección se encuentra en archivos `.py` dentro de las subcarpetas, cargados dinámicamente en la terminal web.
5. Se integró **Pyodide** para permitir la ejecución de Python directamente en el navegador, sin backend.
6. Los cambios se consolidaron y publicaron en [`MirelSIG/python_spike`](https://github.com/MirelSIG/python_spike).

---

## 📖 Contexto académico

| | |
|---|---|
| **Programa** | Bootcamp Desarrollo Web Fullstack |
| **Centro** | Peñascal – Somos F5 |
| **Equipo** | Grupo 3 |
| **Tipo de tarea** | Spike de investigación técnica |
| **Tema** | Manipulación de tipos de datos en Python |
| **Fecha** | Marzo 2026 |

---

*Proyecto desarrollado con fines educativos como parte del proceso de aprendizaje del Bootcamp Peñascal – Somos F5.*
