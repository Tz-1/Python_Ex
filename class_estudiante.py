##Ejemplo de agregacion

class Estudiante:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
        self.cursos = []

    def agregar_cursos(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"Nombre estudiante {self.nombre} / RUT: {self.rut}")
        for i in self.cursos:
            print(i.nombre)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

estu1 = Estudiante("Tomas", 12345678)

curso01 = Curso("Matematicas")
curso02 = Curso("Lenguaje")
curso03 = Curso("Fisica")
curso04 = Curso("Biologia")

estu1.agregar_cursos(curso01)
estu1.agregar_cursos(curso04)

estu1.mostrar_cursos()