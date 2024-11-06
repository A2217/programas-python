## Tercer examen parcial

class Jgd:
    def __init__(self, nom, año_nac, sex, beca):
        self.nom = nom
        self.año_nac = año_nac
        self.sex = sex
        self.beca = beca

    def __str__(self):
        beca_str = "Becado" if self.beca else "Sin Beca"
        return f'Nombre: {self.nom.ljust(20)} AñoNac: {str(self.año_nac).ljust(5)} Sexo: {self.sex.ljust(6)} Becado: {beca_str}'

class Cat:
    def __init__(self, nom, rng, cst):
        self.nom = nom
        self.rng = rng
        self.cst = cst
        self.jugadores = []

    def agregar_jgd(self, jgd):
        self.jugadores.append(jgd)

    def total_ingr(self):
        total = 0
        for jgd in self.jugadores:
            if not jgd.beca:
                total += self.cst
        return total

    def __str__(self):
        return f'Nombre: {self.nom.ljust(10)}   Rango: {self.rng.ljust(15)}  Costo: ${self.cst:,.2f}'


class Acdm:
    def __init__(self, nom, prop, dom):
        self.nom  = nom
        self.prop = prop
        self.dom  = dom
        self.cats = []

    def agregar_cat(self, cat):
        self.cats.append(cat)

    def total_cats(self):
        return len(self.cats)

    def total_h(self):
        return sum(jgd.sex == 'Hombre' for cat in self.cats for jgd in cat.jugadores)

    def total_m(self):
        return sum(jgd.sex == 'Mujer' for cat in self.cats for jgd in cat.jugadores)

    def total_ingr(self):
        return sum(cat.total_ingr() for cat in self.cats)

    def gen_reporte(self):
        rpt = (f"REPORTE DEL CLUB DEPORTIVO\n\n"
               f"Nombre: {self.nom}\n"
               f"Propietario: {self.prop}\n"
               f"Domicilio: {self.dom}\n\n"
               f"Total de Categorías: {self.total_cats()}\n"
               f"Total de Hombres:    {self.total_h()}\n"
               f"Total de Mujeres:    {self.total_m()}\n\n")

        cats_info = '\n'.join([str(cat) for cat in self.cats])
        rpt += f">> Datos generales de las Categorías\n\n{cats_info}\n\n"

        jgds_info = ''
        for cat in self.cats:
            jgds_info += f'> {cat.nom} - {cat.rng} - ({len(cat.jugadores)})\n'
            for jgd in cat.jugadores:
                jgds_info += f'{str(jgd)}\n'
            subtotal = cat.total_ingr()
            jgds_info += f'\n- SubTotal : ${subtotal:,.2f}\n\n'

        rpt += f">> Jugadores por Categoría:\n\n{jgds_info}"
        rpt += f"-> Total : ${self.total_ingr():,.2f}"

        return rpt


def main():
    acdm = Acdm("Academia los cojos", "Pedro navajas", "Por la esquina del viejo barrio")

    cat1 = Cat("Universidad ", "2000/2001/2002", 2500.00)
    cat2 = Cat("Preparatoria", "2006/2007/2008", 900.00)
    cat3 = Cat("Secundaria  ", "2012/2013/2014", 800.00)
    cat4 = Cat("Especial    ", "1980/1985/1990", 4000.00)

    cat1.agregar_jgd(Jgd("Pedro Piedras", 2006, "Hombre", False))
    cat1.agregar_jgd(Jgd("Francisco Gomez", 2007, "Hombre", True))
    cat1.agregar_jgd(Jgd("Patricia Juarez", 2008, "Mujer", False))

    cat2.agregar_jgd(Jgd("Luis Hernandez", 2009, "Hombre", False))
    cat2.agregar_jgd(Jgd("Luis Mendoza", 2010, "Hombre", False))
    cat2.agregar_jgd(Jgd("Luis Murillo", 2011, "Hombre", True))

    cat3.agregar_jgd(Jgd("Andrea Solis", 2012, "Mujer", True))
    cat3.agregar_jgd(Jgd("Marissa Hernandez", 2013, "Mujer", True))
    cat3.agregar_jgd(Jgd("Diana Soto", 2014, "Mujer", False))

    cat4.agregar_jgd(Jgd("Bruno Diaz", 1980, "Hombre", False))
    cat4.agregar_jgd(Jgd("Clark Kent", 1985, "Hombre", False))
    cat4.agregar_jgd(Jgd("Barry Allen", 1990, "Hombre", False))

    acdm.agregar_cat(cat1)
    acdm.agregar_cat(cat2)
    acdm.agregar_cat(cat3)
    acdm.agregar_cat(cat4)

    print(acdm.gen_reporte())

# programa principal

if __name__ == "__main__":
    main()
