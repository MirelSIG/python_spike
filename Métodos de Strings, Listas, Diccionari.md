#  Métodos de Strings, Listas, Diccionarios y Objetos en Python

---

#  1. STRINGS (`str`)

Los strings son **inmutables**. Todos los métodos devuelven un **nuevo string**.

##  Transformación y normalización

| Método      | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `upper()`   | Convierte a MAYÚSCULAS                    | `"hola".upper()`                 |
| `lower()`   | Convierte a minúsculas                    | `"HOLA".lower()`                 |
| `strip()`   | Elimina espacios/caracteres extremos      | `"  hola  ".strip()`             |
| `replace()` | Sustituye texto                           | `"hola".replace("h","H")`        |

---

##  Búsqueda y análisis

| Método      | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `find()`    | Índice de substring o -1                  | `"hola".find("o")`               |
| `count()`   | Cuenta ocurrencias                        | `"banana".count("a")`            |

---

##  División y unión

| Método      | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `split()`   | Divide en lista                           | `"a,b,c".split(",")`             |
| `join()`    | Une lista en string                       | `",".join(["a","b"])`            |

---

##  Slicing (operación, no método)

| Operación   | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `s[i:j]`    | Substring                                 | `"Python"[0:3]`                  |
| `s[::-1]`   | Invertir                                  | `"Python"[::-1]`                 |

---

#  2. LISTAS (`list`)

Las listas son **mutables**. Muchos métodos modifican la lista original.

##  Métodos incluidos en tu lista

| Método      | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `count()`   | Cuenta ocurrencias                        | `[1,2,2].count(2)`               |
| `len()`     | Longitud                                  | `len([1,2,3])`                   |
| slicing     | Extrae sublistas                          | `[10,20,30][1:3]`                |

---

##  Métodos esenciales adicionales

| Método        | Descripción                             | Ejemplo                          |
|---------------|-----------------------------------------|----------------------------------|
| `append()`    | Añade elemento                          | `l.append(4)`                    |
| `extend()`    | Añade varios elementos                  | `l.extend([4,5])`                |
| `insert()`    | Inserta en posición                     | `l.insert(1,"x")`                |
| `pop()`       | Extrae elemento                         | `l.pop()`                        |
| `remove()`    | Elimina por valor                       | `l.remove("x")`                  |
| `sort()`      | Ordena                                  | `l.sort()`                       |
| `reverse()`   | Invierte                                | `l.reverse()`                    |

---

#  3. DICCIONARIOS (`dict`)

Los diccionarios **no** tienen ninguno de los métodos de strings, excepto `len()`.

##  Métodos incluidos en tu lista

| Método      | Descripción                               | Ejemplo                          |
|-------------|-------------------------------------------|----------------------------------|
| `len()`     | Número de claves                          | `len({"a":1,"b":2})`             |

---

##  Métodos esenciales adicionales

| Método        | Descripción                             | Ejemplo                          |
|---------------|-----------------------------------------|----------------------------------|
| `keys()`      | Devuelve claves                         | `d.keys()`                       |
| `values()`    | Devuelve valores                        | `d.values()`                     |
| `items()`     | Pares clave-valor                       | `d.items()`                      |
| `get()`       | Obtiene valor seguro                    | `d.get("x")`                     |
| `update()`    | Fusiona diccionarios                    | `d.update(otro)`                 |
| `pop()`       | Elimina clave                           | `d.pop("x")`                     |
| `setdefault()`| Inserta si no existe                    | `d.setdefault("x",0)`            |

---

#  4. TABLA COMPARATIVA GLOBAL

| Método     | Strings | Listas | Diccionarios | Objetos generales |
|------------|---------|--------|--------------|-------------------|
| `count()`  | ✔️      | ✔️     | ❌           | —                 |
| `len()`    | ✔️      | ✔️     | ✔️           | ✔️                |
| `find()`   | ✔️      | ❌     | ❌           | —                 |
| `split()`  | ✔️      | ❌     | ❌           | —                 |
| `join()`   | ✔️      | ❌     | ❌           | —                 |
| `replace()`| ✔️      | ❌     | ❌           | —                 |
| `strip()`  | ✔️      | ❌     | ❌           | —                 |
| `upper()`  | ✔️      | ❌     | ❌           | —                 |
| `lower()`  | ✔️      | ❌     | ❌           | —                 |
| slicing    | ✔️      | ✔️     | ❌           | —                 |

---

# 5. OTROS MÉTODOS IMPORTANTES

##  Strings

| Método        | Descripción                     |
|---------------|---------------------------------|
| `startswith()`| Verifica prefijo                |
| `endswith()`  | Verifica sufijo                 |
| `isdigit()`   | Solo números                    |
| `isalpha()`   | Solo letras                     |
| `isalnum()`   | Letras y números                |
| `splitlines()`| Divide por saltos de línea      |
| `capitalize()`| Primera letra mayúscula         |
| `title()`     | Formato título                  |
| `casefold()`  | Normalización agresiva          |

---

## 📦 Listas

| Método      | Descripción                     |
|-------------|---------------------------------|
| `clear()`   | Vacía la lista                  |
| `copy()`    | Copia superficial               |
| `index()`   | Índice de un valor              |

---

## Diccionarios

| Método        | Descripción                     |
|---------------|---------------------------------|
| `clear()`     | Vacía el diccionario           |
| `copy()`      | Copia superficial               |
| `fromkeys()`  | Crea dict desde claves          |

---

# FIN DEL DOCUMENTO
