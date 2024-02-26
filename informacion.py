class producto:
    def __init__(self, codigo_producto, nombre_producto, descripcion, precio_unitario):
        self.codigo_producto = codigo_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

class cliente:
    def __init__(self, nombre_cliente, correo, nit):
        self.nombre_cliente = nombre_cliente
        self.correo = correo
        self.nit = nit

class compra:
    def __init__(self, lista_producto, cliente, id, total, impuesto):
        self.lista_producto = lista_producto
        self.cliente = cliente
        self.id = id
        self.total = total
        self.impuesto = impuesto
