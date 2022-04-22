from clases.Alumnos import Fecha,Alumno

alumno = Alumno("Angel",Fecha(18,7,1991))
alumno2 = Alumno("Juan",Fecha(18,7,1991))

alumno.comparaMayor(alumno2)


alumno3 = Alumno("Ana",Fecha(14,3,1990))
alumno4 = Alumno("Carmen",Fecha(8,7,1993))

alumno3.comparaMayor(alumno4)