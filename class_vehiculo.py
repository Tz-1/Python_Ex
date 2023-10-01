class Vehiculo():
    ruedas=4
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color

    def desplazamiento(self):
        print("El vehículo se está desplazando sobre 4 ruedas")



miCarro1 = Vehiculo('Negro', '20')
print (miCarro1.get_color())
miCarro1.set_color('Blanco')
print (miCarro1.get_color())
