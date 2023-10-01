class NuestraExcepcion(Exception):
    def __init__(self, message):
        super().__init__(message)

message = "Salario no se encuentra entre los rangos 1000 y 2000"

salario = int(input("Ingrese salario: "))

if salario <= 1000 or salario >= 2000:
    raise NuestraExcepcion(message)
else:
    print("Se ingresado salario con exito")