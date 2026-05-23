class  RegistroProductos:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("Precio debe ser mayor que cero")
        self.productos[nombre] = {"nombre": nombre, "precio_base": precio_base}
        return "Producto creado exitosamente"
    

    def obtener_producto(self, nombre):
        return self.productos.get(nombre) 
    
    def aplicar_descuento(self, nombre, porcentaje_descuento):
        if porcentaje_descuento <= 0 or porcentaje_descuento > 40:
            raise ValueError("Descuento fuera de rango. Máximo permitido: 40%")
        producto = self.obtener_producto(nombre)
        if producto is None:
            raise ValueError("Producto no encontrado")
        precio_con_descuento = producto["precio_base"] * (1 - porcentaje_descuento / 100)
        return precio_con_descuento
    
    def calcular_precio_final(self, nombre, porcentaje_descuento, iva=0.19):
        precio_con_descuento = self.aplicar_descuento(nombre, porcentaje_descuento)
        precio_final = precio_con_descuento * (1 + iva)
        return precio_final
    
    def verificar_precio_final_positivo(self, nombre, porcentaje_descuento, iva=0.19):
        precio_final = self.calcular_precio_final(nombre, porcentaje_descuento, iva)
        if precio_final <= 0:
            raise ValueError("Precio final no puede ser negativo o cero")
        return precio_final

