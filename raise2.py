class NuestraExcepcion(Exception):
    def __init__(self, message):
        super().__init__(message)

message = "Este es el mensaje de Nuestra Excepción."

def division_entera(x,y):
    if y == 0:
        raise NuestraExcepcion(message)
    else:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor

try:
    resultado = division_entera(1, 0)
    print(resultado)
except NuestraExcepcion:
    print('Error en división por 0')