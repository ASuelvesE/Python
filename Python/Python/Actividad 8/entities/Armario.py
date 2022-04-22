from common.utils import read
# prendas
from entities.Camiseta import Camiseta
from entities.Pantalon import Pantalon
from entities.Zapatillas import Zapatillas

path = './data/datos.xml'


class Armario:
    prendas = []

    def lee(self):
        self.prendas = []
        datos = read(path)
        for prendaData in datos:
            marca = ''
            tipo = prendaData.attrib['tipo']
            if 'marca' in prendaData.attrib:
                marca = prendaData.attrib['marca']
            color = prendaData.attrib['color']
            talla = prendaData.attrib['talla']
            prenda = None
            if tipo == 'camiseta':
                prenda = Camiseta(marca, color, talla)
            elif tipo == 'pantalon':
                prenda = Pantalon(marca, color, talla)
            elif tipo == 'zapatillas':
                prenda = Zapatillas(marca, color, talla)
            self.prendas.append(prenda)
        return self.prendas
