# Aplicaciones orientado a objetos que simule las ventas de una tienda

class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio

    def __str__(self):
        return f'Articulo: {self.articulo:<15} Cantidad: {self.cantidad:>10.2f} Precio: {self.precio:>10,.2f} Total: {self.total:>10,.2f}'

class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = []

    def agregarVenta(self, venta):
        self.ventas.append(venta)

    def totalVentas(self):
        total = 0
        for venta in self.ventas:
            total += venta.total
        return total

    def __str__(self):
        return f'Cliente -> [RFC: {self.rfc}, Nombre: {self.nombre}, Domicilio: {self.domicilio}, Correo: {self.correo}, Total Ventas: {self.totalVentas():,.2f}]'

class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = []

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total

    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total

    def __str__(self):
        return f'Tienda -> [Nombre: {self.nombre}, Domicilio: {self.domicilio}, Propietario: {self.propietario}]'

def capturacliente():
    print("Dame los datos del cliente")
    rfc         = input("RFC        : ")
    nombre      = input("Nombre     : ")
    domicilio   = input("Domicilio  : ")
    correo      = input("Correo     : ")
    cliente     = Cliente(rfc, nombre, domicilio, correo)
    return cliente

def agregarVentas(cliente):
    print("Captura de ventas ", cliente.nombre)
    while True:
        articulo = input("Articulo: ")
        if articulo == '':
            break
        cantidad = float(input("Cantidad: "))
        precio = float(input("Precio: "))
        cliente.agregarVenta(Venta(articulo, cantidad, precio))

def main():    
    print('Inicio del programa en la funcion main() principal:\n')

    mitienda = Tienda(nombre='Ferretería Las Lomas', domicilio='Av Luis Moya 345', propietario='Carlos Castañeda')

    mitienda.agregarCliente(Cliente(rfc='ARTM478950', nombre='Arturo Molina', domicilio='MITA UAZ', correo='correo100%real@msn.com'))
    mitienda.agregarCliente(Cliente(rfc='JELI120240', nombre='Felipe Calderón', domicilio='Las Lomas 123', correo='calde@msn.com'))
    mitienda.agregarCliente(Cliente(rfc='PEÑA121250', nombre='Enrique Peña', domicilio='5 de Mayo 321', correo='quique@gmail.com'))
    mitienda.agregarCliente(Cliente(rfc='AMLO101145', nombre='Andrés López', domicilio='Palacio Nacional 321', correo='peje@yahoo.com'))
    mitienda.agregarCliente(Cliente(rfc='GELA666666', nombre='Xóchitl Gelatinas', domicilio='Danone 123', correo='xochitl@precidencia.gob.mx'))

    mitienda.clientes[0].agregarVenta(Venta(articulo='Cable inalambrico', cantidad=100, precio=5.00))
    mitienda.clientes[1].agregarVenta(Venta(articulo='Martillo', cantidad=10, precio=60.5))
    mitienda.clientes[1].agregarVenta(Venta(articulo='Pala', cantidad=2, precio=1170.55))
    mitienda.clientes[2].agregarVenta(Venta(articulo='Clavo', cantidad=2.5, precio=160.34))
    mitienda.clientes[2].agregarVenta(Venta(articulo='Cinta de Aislar', cantidad=5, precio=71.34))
    mitienda.clientes[3].agregarVenta(Venta(articulo='Abrazos', cantidad=3, precio=100.00))
    mitienda.clientes[4].agregarVenta(Venta(articulo='Presidencia', cantidad=1, precio=5.00))

    # Captura de un nuevo cliente y sus ventas
    nuevo_cliente = capturacliente()
    mitienda.agregarCliente(nuevo_cliente)
    agregarVentas(nuevo_cliente)

    print(f'\nReporte de Ventas: {mitienda}\n')
    print(f'Total de clientes : {len(mitienda.clientes)}')
    print(f'Total ventas : {mitienda.totalVentas()}')

    print('\nClientes:')
    for cliente in mitienda.clientes:
        print(cliente)

    print('\nVentas de cada cliente:')
    for cliente in mitienda.clientes:
        print(f'\n{cliente.rfc} - {cliente.nombre} - {cliente.correo} - Total Ventas: {cliente.totalVentas():,.2f}')
        for venta in cliente.ventas:
            print(f'- {venta}')

    print(f'\nTotal importe ventas : {mitienda.totalImporteVentas():,.2f}')


# Programa principal
if __name__ == '__main__':
    main()
