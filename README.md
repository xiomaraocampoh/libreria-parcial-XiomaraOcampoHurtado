# Análisis de pruebas — Parte 1

Este documento contiene el análisis de particiones de equivalencia y valores límite requeridos para las reglas del caso práctico.

## Regla 1: Precio base mayor que cero

Descripción: El precio base debe ser mayor que cero. Si se intenta crear un producto con precio cero o negativo, el sistema debe rechazarlo con un mensaje claro.

Tabla de particiones de equivalencia:

| Partición | Válida / Inválida | Valor representativo | Resultado esperado |
|---|---:|---|---|
| Precio > 0 | Válida | 100.00 | Producto creado correctamente |
| Precio = 0 | Inválida | 0.00 | Rechazo: "Precio debe ser mayor que cero" |
| Precio < 0 | Inválida | -5.00 | Rechazo: "Precio debe ser mayor que cero" |
| No numérico / nulo | Inválida | "abc" / (campo vacío) | Rechazo: "Precio inválido" |

## Regla 2: Descuento entre 0% y 40%

Descripción: Se puede aplicar un descuento porcentual al producto. El descuento debe estar entre 0% y 40% (incluye 0% y 40%). Descuentos fuera de ese rango deben rechazarse.

Tabla de particiones de equivalencia:

| Partición | Válida / Inválida | Valor representativo | Resultado esperado |
|---|---:|---|---|
| 0% ≤ descuento ≤ 40% | Válida | 0%, 20%, 40% | Descuento aceptado y aplicado |
| descuento < 0% | Inválida | -1% | Rechazo: "Descuento fuera de rango" |
| descuento > 40% | Inválida | 50% | Rechazo: "Descuento fuera de rango" |
| No numérico / nulo | Inválida | "x" / (campo vacío) | Rechazo: "Descuento inválido" |

### Análisis de valores límite para Regla 2

Valores críticos en los bordes del rango 0%–40% (casos de borde):

| Valor de descuento | Tipo (Borde) | Resultado esperado |
|---|---:|---|
| -1% | Borde inferior inválido | Rechazo |
| 0% | Borde inferior válido | Aceptado |
| 1% | Dentro del rango | Aceptado |
| 39% | Dentro del rango | Aceptado |
| 40% | Borde superior válido | Aceptado |
| 41% | Borde superior inválido | Rechazo |
| 40.0001% | Borde superior (precisión) inválido | Rechazo (según precisión definida) |

Nota: Incluir pruebas que verifiquen la precisión y el comportamiento ante valores no enteros (por ejemplo, 12.5%) si la aplicación admite decimales.

## Regla 3: Cálculo del precio final y pregunta al administrador

Descripción: El precio final se calcula aplicando primero el descuento y luego el IVA del 19% sobre el resultado. El precio final nunca puede ser negativo.

Pregunta al administrador (antes de diseñar pruebas):

- ¿Cuál es la política de redondeo para precios (p. ej., redondear a centavos, usar truncamiento, o usar precisión bancaria)?

Justificación: La forma de redondeo afecta el resultado final y puede crear discrepancias en los casos límite y las aserciones de los tests.

---

# PARTE 2 — Casos de prueba (10 minutos) 

Diseña una tabla en el `README.md` con mínimo 8 casos de prueba usando el formato:

```
ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo
```

Los tipos son Positivo, Negativo o Borde. Los 8 casos deben distribuirse entre las tres reglas e incluir al menos dos de borde y al menos dos negativos.

**Regla 1:** Un producto tiene nombre y precio base. El precio base debe ser mayor que cero. Si se intenta crear un producto con precio cero o negativo, el sistema debe rechazarlo con un mensaje claro.

**Regla 2:** Se puede aplicar un descuento porcentual al producto. El descuento debe estar entre 0% y 40%. Un descuento mayor al 40% debe ser rechazado. Un descuento del 0% es válido.

**Regla 3:** El precio final se calcula aplicando primero el descuento y luego el IVA del 19% sobre el resultado. El precio final nunca puede ser negativo.

## Casos de prueba: 

| ID | REGLA | DESCRIPCIÓN | PRECONDICIÓN | DATOS DE ENTRADA | PASOS | RESULTADO ESPERADO | TIPO |
|:-- |:-- |:-- |:-- |:-- |:-- |:-- |:-- |
| T01 | Regla 1 | Crear producto con precio base válido | Sistema listo; no hay productos previos | Nombre: "Laptop", Precio base: $3,500 | 1. Ingresar nombre "Laptop" 2. Ingresar precio base $3,500 3. Confirmar creación | Producto creado exitosamente con nombre "Laptop" y precio base $3,500 | Positivo |
| T02 | Regla 1 | Crear producto con precio mínimo válido (borde) | Sistema listo; no hay productos previos | Nombre: "Artículo", Precio base: $0.01 | 1. Ingresar nombre "Artículo" 2. Ingresar precio base $0.01 3. Confirmar creación | Producto creado exitosamente (borde inferior válido) | Borde |
| T03 | Regla 1 | Rechazar producto con precio cero | Sistema listo; no hay productos previos | Nombre: "Producto", Precio base: $0 | 1. Ingresar nombre "Producto" 2. Ingresar precio base $0 3. Intentar confirmar | El sistema rechaza la creación con mensaje: "Precio debe ser mayor que cero" | Negativo |
| T04 | Regla 2 | Aplicar descuento válido dentro del rango | Producto existente: nombre "Mouse", precio base $100 | Descuento: 20% | 1. Seleccionar producto "Mouse" 2. Ingresar descuento 20% 3. Aplicar descuento | Descuento aplicado correctamente (20% válido) | Positivo |
| T05 | Regla 2 | Aplicar descuento en borde superior (40%) | Producto existente: nombre "Teclado", precio base $200 | Descuento: 40% | 1. Seleccionar producto "Teclado" 2. Ingresar descuento 40% 3. Aplicar descuento | Descuento aplicado correctamente (borde superior válido) | Borde |
| T06 | Regla 2 | Rechazar descuento mayor al 40% | Producto existente: nombre "Monitor", precio base $500 | Descuento: 50% | 1. Seleccionar producto "Monitor" 2. Ingresar descuento 50% 3. Intentar aplicar | El sistema rechaza con mensaje: "Descuento fuera de rango. Máximo permitido: 40%" | Negativo |
| T07 | Regla 3 | Calcular precio final con descuento e IVA correctamente | Producto con precio base $1,000 y descuento 20% | Precio base: $1,000, Descuento: 20%, IVA: 19% | 1. Calcular precio con descuento: $1,000 - 20% = $800 2. Aplicar IVA 19%: $800 × 1.19 = $952 3. Verificar resultado | Precio final calculado: $952 (correcto: ($1,000 - 20%) × 1.19) | Positivo |
| T08 | Regla 3 | Verificar precio final positivo con descuento máximo (borde) | Producto con precio base $100 y descuento 40% | Precio base: $100, Descuento: 40%, IVA: 19% | 1. Calcular precio con descuento máximo: $100 - 40% = $60 2. Aplicar IVA 19%: $60 × 1.19 = $71.40 3. Verificar que sea positivo | Precio final: $71.40 (positivo, borde de descuento máximo) | Borde |