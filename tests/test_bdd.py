import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.productos import RegistroProductos

scenarios('features/productos.feature')

@pytest.fixture
def escenario():
    return {}

@given("un sistema de registro de productos", target_fixture="sistema")
def sistema_inicializado():
    return RegistroProductos()

@given(parsers.parse('un producto llamado "{nombre}" con precio base {precio_base:float}'))
def producto_registrado(sistema, escenario, nombre, precio_base):
    sistema.registrar_producto(nombre, precio_base)
    escenario["nombre"] = nombre

@given("que soy administrador de la librería")
def administrador_de_la_libreria():
    return True

@given("el sistema de registro de productos está disponible")
def sistema_disponible(sistema):
    assert sistema is not None
    return True

@when(parsers.parse('intento aplicar un descuento de {descuento:float}%'))
def intento_aplicar_descuento(sistema, escenario, descuento):
    try:
        precio_con_descuento = sistema.aplicar_descuento(escenario["nombre"], descuento)
        escenario["estado"] = "aceptado"
        escenario["precio_final"] = round(precio_con_descuento, 2)
    except ValueError:
        escenario["estado"] = "rechazado"
        escenario["precio_final"] = None

@when(parsers.parse('intento aplicar un descuento con valor "{valor_descuento}"'))
def intento_aplicar_descuento_valor(sistema, escenario, valor_descuento):
    try:
        if not valor_descuento.endswith('%'):
            raise ValueError("porcentaje inválido")
        porcentaje = float(valor_descuento[:-1])
        sistema.aplicar_descuento(escenario["nombre"], porcentaje)
    except (ValueError, TypeError):
        escenario["error"] = "porcentaje inválido"

@then(parsers.parse('el estado debe ser "{estado}"'))
def verificar_estado(escenario, estado):
    assert escenario.get("estado") == estado

@then(parsers.parse('el precio final debe ser {precio_final}'))
def verificar_precio_final(escenario, precio_final):
    if precio_final == "-":
        assert escenario.get("precio_final") is None
    else:
        assert escenario.get("precio_final") == pytest.approx(float(precio_final))

@then(parsers.parse('el sistema debe devolver un error indicando "{mensaje}"'))
def verificar_error(escenario, mensaje):
    assert mensaje in escenario.get("error", "")
 
