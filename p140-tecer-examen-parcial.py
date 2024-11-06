## Tercer examen parcial

class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        beca_str = "Becado" if self.becado else "Sin Beca"
        return f'Nombre: {self.nombre.ljust(20)} AñoNac: {str(self.año_nac).ljust(5)} Sexo: {self.sexo.ljust(6)} Becado: {beca_str}'

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def total_ingresos(self):
        total = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                total += self.costo
        return total

    def __str__(self):
        return f'Nombre: {self.nombre.ljust(10)}   Rango: {self.rango.ljust(15)}  Costo: ${self.costo:,.2f}'


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre      = nombre
        self.propietario = propietario
        self.domicilio   = domicilio
        self.categorias  = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_categorias(self):
        return len(self.categorias)

    def total_hombres(self):
        return sum(jugador.sexo == 'Hombre' for categoria in self.categorias for jugador in categoria.jugadores)

    def total_mujeres(self):
        return sum(jugador.sexo == 'Mujer' for categoria in self.categorias for jugador in categoria.jugadores)

    def total_ingresos(self):
        total = sum(categoria.total_ingresos() for categoria in self.categorias)
        return total

    def generar_reporte(self):
        reporte = (f"REPORTE DEL CLUB DEPORTIVO\n\n"
                   f"Nombre: {self.nombre}\n"
                   f"Propietario: {self.propietario}\n"
                   f"Domicilio: {self.domicilio}\n\n"
                   f"Total de Categorías: {self.total_categorias()}\n"
                   f"Total de Hombres: {self.total_hombres()}\n"
                   f"Total de Mujeres: {self.total_mujeres()}\n\n")

        categorias_info = '\n'.join([str(categoria) for categoria in self.categorias])
        reporte += f">> Datos generales de las Categorías\n\n{categorias_info}\n\n"
    
        jugadores_info = ''
        for categoria in self.categorias:
            jugadores_info += f'> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})\n'
            for jugador in categoria.jugadores:
                jugadores_info += f'{str(jugador)}\n'
            subtotal = categoria.total_ingresos()
            jugadores_info += f'\n- SubTotal : ${subtotal:,.2f}\n\n'

        reporte += f">> Jugadores por Categoría:\n\n{jugadores_info}"
        reporte += f"-> Total : ${self.total_ingresos():,.2f}"

        return reporte


def main():
    academia = Academia("Academia los cojos", "Pedro navajas", "Por la esquina del viejo barrio")

    cat1 = Categoria("Universidad ", "2000/2001/2002", 2500.00)
    cat2 = Categoria("Preparatoria", "2006/2007/2008", 900.00)
    cat3 = Categoria("Secundaria  ", "2012/2013/2014", 800.00)
    cat4 = Categoria("Especial    ", "1980/1985/1990", 4000.00)

    cat1.agregar_jugador(Jugador("Pedro Piedras", 2006, "Hombre", False))
    cat1.agregar_jugador(Jugador("Francisco Gomez", 2007, "Hombre", True))
    cat1.agregar_jugador(Jugador("Patricia Juarez", 2008, "Mujer", False))

    cat2.agregar_jugador(Jugador("Luis Hernandez", 2009, "Hombre", False))
    cat2.agregar_jugador(Jugador("Luis Mendoza", 2010, "Hombre", False))
    cat2.agregar_jugador(Jugador("Luis Murillo", 2011, "Hombre", True))

    cat3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    cat3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    cat3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))

    cat4.agregar_jugador(Jugador("Bruno Diaz", 1980, "Hombre", False))
    cat4.agregar_jugador(Jugador("Clark Kent", 1985, "Hombre", False))
    cat4.agregar_jugador(Jugador("Barry Allen", 1990, "Hombre", False))

    academia.agregar_categoria(cat1)
    academia.agregar_categoria(cat2)
    academia.agregar_categoria(cat3)
    academia.agregar_categoria(cat4)

    print(academia.generar_reporte())

#programa principal

if __name__ == "__main__":
    main()
