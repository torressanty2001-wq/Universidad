class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print(f"Sí hay {cantidad} unidades disponibles de {self.nombre}")
            return True
        else:
            print(f"No hay suficientes unidades de {self.nombre}")
            return False

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}")
            print(f"Stock restante: {self.stock}")
        else:
            print("No hay suficiente stock para realizar la venta")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} unidades al stock")
        print(f"Nuevo stock: {self.stock}")


# Crear objeto
producto1 = Producto("Laptop", 1200, 10)

# Operaciones solicitadas
producto1.verificar_disponibilidad(5)

producto1.vender(3)

producto1.verificar_disponibilidad(8)

producto1.vender(8)

producto1.reabastecer(10)

producto1.verificar_disponibilidad(8)

producto1.vender(8)