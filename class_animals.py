class Animal:

    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def caminar(self):
        print(f"{self.nombre} esta caminando.")

    def comer(self):
        print(f"{self.nombre} esta comiendo.")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo.")

perro = Animal("Brando","San Bernando", 3, 30)

gato = Animal("Roll", "Persa", 4, 3)

perro.comer()
gato.dormir()