while True:
    try:
        edad = int(input("Ingrese su edad: "))
    except:
        print("Debe ingresar un numero. Intentelo de nuevo")
    else:
        if edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")
        break
