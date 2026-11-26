# Programación I · Laboratorio 11: de funciones a objetos

**Modalidad: individual · Escribir todo el código desde cero**

## Identificación (completa antes del primer ejercicio)

- **Nombre y apellido: Carlos palmero**
- **Fecha: 25 Nov. 2026**
- **URL del repositorio: https://github.com/kakePalmerow/Labo11.git**

## Objetivos

Construir clases y objetos en Python, comprender `__init__` y `self`, crear métodos y validar operaciones, reutilizar listas/diccionarios y registrar avances con Git.

## Preparación de repositorio — ¡IMPORTANTE!

1. En la plantilla de la profesora, haz clic en **Use this template → Create a new repository**.
2. Crea un repositorio **privado** en tu propia cuenta con nombre `Lab11-POO`.
3. Completa la identificación arriba **en tu copia**. No agregues cédulas, contraseñas, tokens ni información sensible.
4. En **Settings → Collaborators → Add people**, invita a la profesora usando el usuario GitHub ameneses-uma y confirma que la invitación está pendiente/aceptada.
5. Clona **tu** repositorio desde VS Code o terminal: `git clone URL_DE_TU_REPOSITORIO`.
6. Abre la carpeta clonada, ejecuta `git status` y comprueba que estás dentro del repositorio correcto.
7. Guarda tus cambios: `git add README.md`, `git commit -m "Identificación"`, `git push -u origin main` (si tu rama es `main`; de lo contrario usa el nombre real de tu rama).

> **No clones la plantilla original para entregar allí.** Tu trabajo debe estar en tu repositorio personal creado con **Use this template**. A diferencia de `git clone`, ese paso crea una copia propia en GitHub.

## Normas de trabajo

- Los archivos `.py` están deliberadamente **vacíos**: escribe todo el código, incluido `class`, `def`, `__init__`, `self` y la ejecución.
- Resuelve el ejercicio primero; **predice**, **ejecuta**, **corrige** y después registra tu avance.
- No copies de otros repositorios ni entregues código que no puedas explicar.
- Puedes consultar apuntes y documentación del curso.
- Toda asistencia externa debe ajustarse a las reglas de la asignatura.
- Al final de cada etapa: `git status` → `git add <archivo>` → `git commit -m "..."` → `git push`.
- Comprueba en GitHub que tus commits y archivos estén visibles en **tu repositorio**.
- En `respuestas/respuestas.md` escribe las predicciones y respuestas; no modifiques ese archivo solo para poner "listo".

## Ejercicio 1

**Archivo:** `ejercicios/01_diccionarios.py`

Desde cero: representa dos cuentas con diccionarios (`titular`, `saldo`). Escribe una función `depositar(cuenta, monto)` que agregue el monto solo si es mayor que cero y retorne `True` si tuvo éxito, `False` en caso contrario. Haz un depósito válido a la primera cuenta y uno inválido a la segunda. Imprime ambos saldos. **Antes de ejecutar** anota resultados esperados en `reflexiones/respuestas.md`.

**Comprobación:** depósito válido modifica solo su cuenta; monto no positivo no modifica el saldo.

**Commit sugerido:** `Resolver cuentas con diccionarios`

## Ejercicio 2

**Archivo:** `ejercicios/02_cuenta_bancaria.py`

Escribe completamente una clase `CuentaBancaria` con constructor para `titular` y `saldo`. Crea dos objetos con datos distintos. Imprime sus atributos y modifica directamente el saldo de **uno** para demostrar que no cambia el otro. Agrega comentario que explique qué hace `self` y cuál es la diferencia entre clase e instancia. **No implementes todavía depósitos ni retiros**: eso corresponde a la etapa 3.

**Comprobación:** objetos diferentes mantienen estados independientes.

**Commit sugerido:** `Construir clase CuentaBancaria`

## Ejercicio 3

**Archivo:** `ejercicios/03_metodos.py`

**Reescribe desde cero** la clase `CuentaBancaria` en este archivo (no hagas copy/paste de la anterior). Incluye constructor y métodos:

- `depositar(monto)` retorna booleano: acepta solo monto positivo.
- `retirar(monto)` retorna booleano: acepta solo monto positivo que no supere saldo.
- `consultar_saldo()` devuelve el saldo actual.

Comprueba con una cuenta inicial de 500 las operaciones `depositar(100)`, `retirar(200)` y `retirar(600)`. Predice y verifica el resultado final y los booleanos retornados. Muestra un mensaje claro para un intento inválido. **No uses `input()` en esta etapa**: utiliza casos de prueba fijos para concentrarte en los objetos.

**Commit sugerido:** `Agregar metodos y validaciones`

## Ejercicio 4

**Archivo:** `ejercicios/04_persona.py`

Implementa desde cero clase `Persona` con atributos `nombre`, `edad`, `carrera`; métodos `presentarse()` (devuelve texto), `cumplir_anios()` (aumenta uno) y `es_mayor_de_edad()` (devuelve booleano). Crea dos personas de distintas carreras. Imprime presentaciones y prueba la transición de 17 a 18 años. Define qué ocurre si alguien es creado con edad negativa: aplica una validación sencilla y explícala en `respuestas.md`.

**Commit sugerido:** `Implementar clase Persona`

## Ejercicio 5

**Archivo:** `ejercicios/05_lista_objetos.py`

Escribe de nuevo una clase `Persona` mínima (constructor y `es_mayor_de_edad`) y crea una lista con **cuatro objetos**. Utiliza un ciclo para imprimir los nombres, cuenta mayores de edad, construye una lista filtrada por carrera y calcula el promedio de edad. Evita dividir entre cero en el caso de una lista vacía. **Extensión opcional:** función que recibe la lista de objetos y devuelve la persona de mayor edad.

**Commit sugerido:** `Integrar listas y objetos`

## Etapa final | Comprobar y responder

1. Ejecuta cada archivo con `python ejercicios/NOMBRE.py` (o `python3` según el equipo).
2. Registra en `respuestas/respuestas.md`: (a) clase vs objeto; (b) para qué sirve `self`; (c) un error que corregiste; (d) qué dudas llevas al jueves.
3. Haz commit/push de reflexiones: `Registrar respuesta del laboratorio`.
4. Revisa en GitHub que aparecen todos los archivos y commits; responde el formulario de salida.

## Mini recordatorio Git

```bash
git status
git add ejercicios/03_metodos.py
git commit -m "feat: agregar metodos y validaciones"
git push

git log --oneline -7
```

> `git add` selecciona cambios; `git commit` los guarda localmente; `git push` publica los commits en GitHub. Si el primer `push` requiere indicar upstream, usa `git push -u origin main` en una rama llamada `main`.

## Criterios de revisión formativa

Se revisará evidencia de código **propio y ejecutable**, comportamiento correcto, explicación de decisiones, historial coherente y sincronización en GitHub.
