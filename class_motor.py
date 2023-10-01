#Composicion (contiene) trabaja juntos y se necesitan
#agregacion puede existir de forma independiente pero pueden trabajar juntos
class Motor():
    def __init__(self, cilindros):
        self.encendido = False
        self.cilindros = cilindros

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

class Auto():
    def __init__(self):
        self.motor = Motor(6)

    def encender_auto(self):
        self.motor.encender()

    def apagar_auto(self):
        self.motor.apagar()

    def consultar_estado(self):
        return self.motor.encendido


miauto = Auto()

print(miauto.consultar_estado())

miauto.encender_auto()

print(miauto.consultar_estado())