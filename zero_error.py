def division_entera(x,y):
    if y == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    dividendo = int(x)
    divisor = int(y)
    return dividendo/divisor

resultado = division_entera(1, 0)
print(resultado)
