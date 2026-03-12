# Plataforma Educativa Python con Consola Bash Simulada

Este proyecto es una plataforma web educativa para practicar Python desde el navegador.
El usuario puede editar scripts, ejecutarlos en tiempo real y ver la salida en una consola visual que simula una terminal Bash.

## Objetivo

Facilitar el aprendizaje de conceptos basicos de Python mediante ejemplos interactivos, sin necesidad de instalar Python localmente.

## Como funciona

1. El usuario elige un tema (por ejemplo, `Strings`, `Listas` o `Pathlib`).
2. El sistema carga un archivo `.py` de ejemplo dentro de un editor en pantalla.
3. Al presionar `Ejecutar script`, el codigo se ejecuta con **Pyodide** (Python en WebAssembly dentro del navegador).
4. La salida (`stdout`) y errores (`stderr`) se muestran en una terminal visual estilo Bash.

## Caracteristicas principales

- Ejecucion de codigo Python directamente en el navegador.
- Consola simulada con prompt estilo Bash (`usuario@host:~$`).
- Editor integrado para modificar el codigo antes de ejecutarlo.
- Demos incluidos: `Strings`, `Listas` y multiples casos de `Pathlib`.
- Botones de control:
- `Ejecutar script`
- `Limpiar`
- Cambio de tema visual (modo oscuro y claro).
- Navegacion por secciones de distintos integrantes del equipo.

## Tecnologias usadas

- `HTML5`
- `CSS3`
- `JavaScript` (logica del editor y terminal)
- `Pyodide` (motor de ejecucion Python en el cliente)

## Estructura general del proyecto

- `MirelPY/`, `LuisPY/`, `JuanCarlosPY/`: secciones por integrante.
- Cada seccion incluye:
- `index.html`: interfaz de usuario.
- `index.css`: estilos visuales.
- `terminal.js`: logica de carga y ejecucion de scripts.
- Subcarpetas tematicas con archivos `.py` de ejemplo.
- En `MirelPY/` se incluyen ejemplos en:
- `metodos-strings/strings_basicos.py`
- `metodos-listas/listas_basicas.py`
- `metodos-pathlib/pathlib_basicos.py`
- `metodos-pathlib/pathlib_rutas.py`
- `metodos-pathlib/pathlib_archivos.py`
- `metodos-pathlib/pathlib_busqueda.py`
- `Navbar/`: barra de navegacion compartida.

## Demos adicionales de Pathlib

Se agregaron demos practicas de `pathlib` enfocadas en tareas comunes de un developer:

- `pathlib_basicos.py`: introduccion a construccion de rutas, validaciones (`exists`, `is_file`) y metadatos (`name`, `suffix`).
- `pathlib_rutas.py`: navegacion y analisis de rutas (`resolve`, `parts`, `parent`, `relative_to`).
- `pathlib_archivos.py`: flujo diario de archivos (crear carpeta, escribir, leer, renombrar y eliminar archivo).
- `pathlib_busqueda.py`: busqueda de archivos con `glob` y `rglob`, incluyendo filtros por patron.

Estas demos se pueden abrir desde el selector de ejemplos en `MirelPY/index.html` y ejecutar directamente en la consola simulada.

## Flujo tecnico simplificado

- `fetch()` carga el archivo Python original en el editor.
- El contenido editado del `textarea` se toma como script a ejecutar.
- `sys.stdout` y `sys.stderr` se redirigen a buffers en memoria.
- Pyodide ejecuta el script con `runPython(...)`.
- El resultado se imprime en la terminal simulada.

## Uso rapido

1. Abrir una seccion, por ejemplo: `MirelPY/index.html`.
2. Seleccionar un tema de Python (`Strings`, `Listas` o alguna demo de `Pathlib`).
3. Editar el codigo en el editor.
4. Presionar `Ejecutar script`.
5. Revisar salida o errores en la consola simulada.

## Proposito academico

Este repositorio esta orientado a demostraciones y practica inicial de Python.
La experiencia busca imitar una terminal real para reforzar el aprendizaje de comandos y lectura de salida en consola.
