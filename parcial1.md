---

**EXAMEN PARCIAL — CORTE 1**
**Asignatura: Pruebas de Software | Semestre V**
**Tiempo: 60 minutos**
**Entrega: Repositorio GitHub público**
**Nota máxima: 5.0**

---

**LEE ESTO ANTES DE EMPEZAR**

El examen tiene dos secciones: una práctica y una teórica. Ambas se entregan dentro del mismo repositorio de GitHub. Administra el tiempo con cuidado. Se recomienda empezar por la teoría mientras el entorno se configura, o hacerlas en paralelo.

La sección teórica se entrega como un archivo llamado `TEORIA.md` en la raíz del repositorio. Las respuestas deben estar escritas con tus propias palabras. Respuestas copiadas de internet o de otro compañero anulan la sección completa.

Usa el lenguaje y las herramientas de tu preferencia para la sección práctica.

---

**CONTEXTO DEL CASO PRÁCTICO**

La Librería del Centro quiere un módulo para calcular el precio final de sus productos. El administrador entregó estas tres reglas:

**Regla 1:** Un producto tiene nombre y precio base. El precio base debe ser mayor que cero. Si se intenta crear un producto con precio cero o negativo, el sistema debe rechazarlo con un mensaje claro.

**Regla 2:** Se puede aplicar un descuento porcentual al producto. El descuento debe estar entre 0% y 40%. Un descuento mayor al 40% debe ser rechazado. Un descuento del 0% es válido.

**Regla 3:** El precio final se calcula aplicando primero el descuento y luego el IVA del 19% sobre el resultado. El precio final nunca puede ser negativo.

No existe ningún código todavía.

---

## SECCIÓN TEÓRICA — 2.0 puntos
### Archivo: `TEORIA.md` en el repositorio

---

**PREGUNTAS DE SELECCIÓN MÚLTIPLE**
*Escribe el ID de la respuesta correcta y explica en una línea por qué las otras son incorrectas.*

**SM-1 (0.3 puntos)**

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

C. Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.

---

**SM-2 (0.3 puntos)**

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.

C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.

---

**PREGUNTAS ABIERTAS**
*Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

**PA-1 (0.3 puntos)**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

---

**PA-4 (0.2 puntos)**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

---

## SECCIÓN PRÁCTICA — 3.0 puntos

---

**PARTE 0 — Setup (5 minutos) — incluido en los puntos de las demás partes**

Crea el repositorio con el nombre `libreria-parcial-[tunombre]`. Configura el proyecto con tu tecnología de preferencia, agrega las dependencias necesarias y crea la estructura de carpetas separando código de producción y tests. Primer commit solo con configuración, sin lógica.

---

**PARTE 1 — Análisis en el README (10 minutos) — 0.5 puntos**

Antes de escribir cualquier test o código documenta en el `README.md` lo siguiente.

Para la Regla 1 y la Regla 2, una tabla de particiones de equivalencia con todas las particiones válidas e inválidas, el valor representativo de cada una y el resultado esperado.

Para la Regla 2, una tabla de análisis de valores límite con los valores críticos en los bordes del rango 0%-40%.

Para la Regla 3, una pregunta concreta que le harías al administrador antes de diseñar las pruebas, con su justificación en una línea.

Haz commit del análisis antes de escribir código.

---

**PARTE 2 — Casos de prueba (10 minutos) — 0.7 puntos**

Diseña una tabla en el `README.md` con mínimo 8 casos de prueba usando el formato:

```
ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo
```

Los tipos son Positivo, Negativo o Borde. Los 8 casos deben distribuirse entre las tres reglas e incluir al menos dos de borde y al menos dos negativos.

Haz commit cuando la tabla esté completa.

---

**PARTE 3 — TDD (25 minutos) — 1.1 puntos**

Implementa las tres reglas usando el ciclo Red-Green-Refactor. El historial de commits es parte de la nota.

Por cada regla: escribe los tests y haz commit indicando 🔴 RED, escribe el código mínimo para que pasen y haz commit indicando 🟢 GREEN, mejora sin romper nada y haz commit indicando 🔵 REFACTOR.

Los tests deben cubrir los casos diseñados en la Parte 2. Cada test prueba una sola cosa y tiene nombre descriptivo.

Al finalizar ejecuta el reporte de cobertura. Debe superar el 80%. Pega el output en el README.

---

**PARTE 4 — BDD en Gherkin (10 minutos) — 0.7 puntos**

Escribe un archivo `.feature` para las Reglas 2 y 3 con mínimo 5 escenarios. Debe incluir la declaración `Feature` con contexto del usuario en lenguaje de negocio, `Background` si aplica, al menos un `Scenario Outline` con tabla `Examples`, al menos un escenario de error y tags en todos los escenarios.

Implementa los step definitions conectados al código de la Parte 3. Todos los escenarios deben pasar.

---

## TABLA DE VALORACIÓN COMPLETA

| Sección | Criterio | Valor |
|---|---|---|
| **TEÓRICA** | SM-1: Selección múltiple con justificación | 0.3 |
| | SM-2: Selección múltiple con justificación | 0.3 |
| | PA-1: TDD ciclo GREEN y su propósito | 0.3 |
| | PA-2: Diferencia TDD vs BDD | 0.3 |
| | PA-3: Cobertura no garantiza ausencia de bugs | 0.3 |
| | PA-4: Por qué probar valores límite | 0.2 |
| | PA-5: Conexión TDD/BDD con CI/CD | 0.3 |
| **Subtotal teórica** | | **2.0** |
| **PRÁCTICA** | Análisis en README: particiones, límites, pregunta | 0.5 |
| | Tabla de 8 casos de prueba correctos y distribuidos | 0.7 |
| | Commits que evidencian ciclo 🔴🟢🔵 por cada regla | 0.3 |
| | Tests completos con cobertura ≥ 80% | 0.5 |
| | Implementación correcta de las 3 reglas | 0.3 |
| | Gherkin con 5 escenarios en lenguaje de negocio | 0.4 |
| | Step definitions funcionando | 0.3 |
| **Subtotal práctica** | | **3.0** |
| **TOTAL** | | **5.0** |

---

**ENTREGA**

El repositorio debe contener al cierre del tiempo:

- `README.md` con el análisis y la tabla de casos de prueba
- `TEORIA.md` con las respuestas a las 7 preguntas
- El código de producción y los tests en la estructura correcta
- El archivo `.feature` y los step definitions
- Mínimo 8 commits con mensajes descriptivos

Publica el link en el foro del curso exactamente cuando el docente indique el cierre. No se reciben repositorios enviados después.