Feature: Reglas 2 y 3 - Gestión de descuentos
    Como administrador de la librería quiero que el sistema valide los descuentos
    aplicados a productos según las Reglas 2 y 3 para asegurar precios finales correctos.

    Background:
        Dado que soy administrador de la librería
        Y el sistema de registro de productos está disponible

    @regla2 @regla3 @positivo
    Scenario: Aplicar descuento válido simple
        Dado un producto llamado "Libro Alpha" con precio base 100.00
        Cuando intento aplicar un descuento de 10%
        Entonces el estado debe ser "aceptado"
        Y el precio final debe ser 90.00

    @regla2 @regla3 @outline
    Scenario Outline: Validar rango y precisión de descuentos (varios casos)
        Dado un producto llamado "<nombre>" con precio base <precio_base>
        Cuando intento aplicar un descuento de <descuento>%
        Entonces el estado debe ser "<estado>"
        Y el precio final debe ser <precio_final>

    Examples:
        | nombre   | precio_base | descuento | estado     | precio_final |
        | Libro A  | 100.00      | -1        | rechazado  | -            |
        | Libro B  | 100.00      | 0         | rechazado  | -            |
        | Libro C  | 100.00      | 1         | aceptado   | 99.00        |
        | Libro D  | 100.00      | 39        | aceptado   | 61.00        |
        | Libro E  | 100.00      | 40        | aceptado   | 60.00        |
        | Libro F  | 100.00      | 41        | rechazado  | -            |
        | Libro G  | 100.00      | 40.0001   | rechazado  | -            |

    @regla2 @regla3 @negativo
    Scenario: Intentar aplicar descuento con formato inválido
        Dado un producto llamado "Libro Beta" con precio base 50.00
        Cuando intento aplicar un descuento con valor "abc%"
        Entonces el sistema debe devolver un error indicando "porcentaje inválido"

    @regla2 @regla3 @boundary
    Scenario: Descuento en límite superior aceptado
        Dado un producto llamado "Libro Límite" con precio base 200.00
        Cuando intento aplicar un descuento de 40%
        Entonces el estado debe ser "aceptado"
        Y el precio final debe ser 120.00


