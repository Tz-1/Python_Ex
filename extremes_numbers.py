def extremos(datos):
    maximo = max(datos)
    minimo = min(datos)
    return minimo, maximo

datos = [5,-2,3,7,0,-1]

a, b = extremos(datos)

print(a,b)

#Function can be called when inside but not define