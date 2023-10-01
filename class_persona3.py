class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        print(f"{self.nombre} esta Caminando")

class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print(f"{self.nombre} esta Trotando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print(f"{self.nombre} esta Rodando")

persona1 = Persona("Vlad")
persona2 = Maratonista("Miguel")
persona3 = Ciclista("さくら") 

persona1.movimiento()
persona2.movimiento()
persona3.movimiento()

#Polimorfismo es solo para metodos
#Sobrecarga

#Para elminiar atributo se elimina en def __init__ y se le agrega un string vacio "" en super()
