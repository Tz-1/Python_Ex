class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get_edad(self):
        return self.edad
    
    def get_apellidos(self):
        return self.apellidos
    
    def set_edad(self, edad):
        self.edad = edad

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos


Persona1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg")
print(Persona1.get_edad())
Persona1.set_edad("21 años")

Persona2 = Persona("Juan", "Camargo", "Masculino", "18 años", "1.8 mts", "75 Kg")
print(Persona2.get_apellidos())
Persona2.set_apellidos("Santiago")

print(Persona1.get_edad())
print(Persona2.get_apellidos())