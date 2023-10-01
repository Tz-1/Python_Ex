#sobrecarga de metodo
class Animal:
    def __init__(self,tipo, especie):
        self.especie = especie
        self.tipo = tipo

    def hacer_sonido(self):
        print("Se hace un sonido generico")

class Perro(Animal):

    def hacer_sonido(self):
        print("Guau! Guau!")

class Gato(Animal):
    
    def hacer_sonido(self):
        print("Meow! Meow!")

class Pollo(Animal):
    
    def hacer_sonido(self):
        print("Pio! Pio!")

perro01 = Perro("Mamifero", "Canino")

gato01 = Gato("Mamifero", "Felino")

pollo01 = Pollo("Ave", "Oviparo")

perro01.hacer_sonido()