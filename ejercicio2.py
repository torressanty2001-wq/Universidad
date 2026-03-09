#REGISTRO DE ESTUDIANTES#
class estudiantes():
    def __init__ (self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    
    def notas(self):
        if self.calificacion == 5:
            print( "aprobado")
        elif self.calificacion >= 4:
            print("aprobado")
        else:
            print("reprobado") 
                
estudiante1 =  estudiantes("santiago" , 24, 5)         
estudiante2 = estudiantes("Carlos", 20 , 5)
estudiante3 = estudiantes("julio", 35, 4)
estudiante1.notas()
estudiante2.notas()
estudiante3.notas()           