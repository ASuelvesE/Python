
class Coche:
    def __init__(self,modelo,velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    def tiempoRecorrido(self,distancia):
        return (distancia / self.velocidad) * 60  #Ej: 500km / 100km/h  = 5 horas 