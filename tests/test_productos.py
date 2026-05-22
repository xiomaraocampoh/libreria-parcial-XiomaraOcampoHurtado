import pytest
from src.productos import RegistroProductos


def test_crear_producto_con_precio_base_valido():
    registro = RegistroProductos()
    resultado = registro.registrar_producto("Laptop", 3500.00)
    assert resultado == "Producto creado exitosamente"

    producto = registro.obtener_producto("Laptop")
    assert producto is not None
    assert producto["nombre"] == "Laptop"
    assert producto["precio_base"] == pytest.approx(3500.00)


def test_crear_producto_con_precio_minimo_valido_borde():
    registro = RegistroProductos()
    resultado = registro.registrar_producto("Artículo", 0.01)
    assert resultado == "Producto creado exitosamente"

    producto = registro.obtener_producto("Artículo")
    assert producto is not None
    assert producto["precio_base"] == pytest.approx(0.01)


def test_rechazar_producto_con_precio_cero():
    registro = RegistroProductos()
    with pytest.raises(ValueError, match="Precio debe ser mayor que cero"):
        registro.registrar_producto("Producto", 0)


def test_aplicar_descuento_valido_dentro_del_rango():
    registro = RegistroProductos()
    registro.registrar_producto("Mouse", 100.00)

    precio_descuento = registro.aplicar_descuento("Mouse", 20.0)
    assert precio_descuento == pytest.approx(80.00)


def test_aplicar_descuento_borde_superior_40_por_ciento():
    registro = RegistroProductos()
    registro.registrar_producto("Teclado", 200.00)

    precio_descuento = registro.aplicar_descuento("Teclado", 40.0)
    assert precio_descuento == pytest.approx(120.00)


def test_rechazar_descuento_mayor_al_40_por_ciento():
    registro = RegistroProductos()
    registro.registrar_producto("Monitor", 500.00)

    with pytest.raises(ValueError, match="Descuento fuera de rango. Máximo permitido: 40%"):
        registro.aplicar_descuento("Monitor", 50.0)


def test_alcular_precio_final_con_descuento_e_iva_correctamente():
    registro = RegistroProductos()
    registro.registrar_producto("Producto", 1000.00)

    precio_final = registro.calcular_precio_final("Producto", 20.0, iva=0.19)
    assert precio_final == pytest.approx(952.00)


def test_verificar_precio_final_positivo_con_descuento_maximo_borde():
    registro = RegistroProductos()
    registro.registrar_producto("Producto", 100.00)

    precio_final = registro.calcular_precio_final("Producto", 40.0, iva=0.19)
    assert precio_final == pytest.approx(71.40)
    assert precio_final > 0
