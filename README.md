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

Commit: análisis inicial para la Parte 1 (README actualizado con particiones y límites).

