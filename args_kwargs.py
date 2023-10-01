def funcion1(param1, *param2):
    print(param1)
    print(param2)
    return

def funcion2(param1, **param2):
    print(param1)
    print(param2)
    return

funcion1(1,2,3,4,5) # param2 se convierte en una tupla

funcion2(1,a=2,b=3,c=4) #param2 se convierte en diccionario (se requiere var)