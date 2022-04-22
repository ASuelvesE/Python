

class Fecha:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano



class Alumno:

    def __init__(self,nombre,Fecha):
        self.Nombre = nombre
        self.Fecha = Fecha

    def comparaMayor(self,alumno):
        if self.Fecha.ano < alumno.Fecha.ano:
            print("Es mayor")
        elif self.Fecha.ano > alumno.Fecha.ano:
            print("Es menor")
        else:
            if self.Fecha.mes < alumno.Fecha.mes:
                print("Es mayor")
            elif self.Fecha.mes > alumno.Fecha.mes:
                print("Es menor")
            else:
                if self.Fecha.dia < alumno.Fecha.dia:
                    print("Es mayor") 
                elif self.Fecha.dia > alumno.Fecha.dia:
                    print("Es menor") 
                else:
                    print("Son iguales.Cumplen los anios el mismo dia")