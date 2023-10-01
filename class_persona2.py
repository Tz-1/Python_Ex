class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarce(self):
        print(f"{self.nombre} se esta concentrando.")

    def viajar(self):
        print(f"{self.nombre} se esta preparando para viajar.")

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self. demarcacion = demarcacion

    def jugarPartido(self):
        print(f"{self.nombre} jugara en el siguiente partido.")

    def entrenar(self):
        print(f"{self.nombre} esta entrenando para el siguiente partido.")

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion

    def dirigirPartido(self):
        print(f"{self.nombre} dirigira el siguiente partido.")

    def dirigirEntrenamiento(self):
        print(f"{self.nombre} dirigira el siguiente entrenamiento.")

class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia

    def darMasajes(self):
        print(f"{self.nombre} dara los masajes.")
