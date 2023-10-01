def ejer01():
    teo = float(input("Ingrese la nota de teoria: "))
    pract = float(input("Ingrese la nota de practica: "))

    prom = (teo + pract) / 2

    if prom >=4:
        print(f"Su nota es {prom} y aprobo la materia")
    else:
        print(f"Su nota es {prom} y reprobo la materia")

def ejer02():
    cel = int(input("Ingrese los grados Celsius: "))

    faren = 1.8 * cel + 32

    print(f"Los grados farenheit son: {faren}") 

def ejer03():
    peso = float(input("Ingrese su peso: "))

    altura = float(input("Ingrese su altura: "))

    imc = peso / altura**2

    print(f"Su IMC es de: {imc:.1f}") #print(round(imc,2))

def ejer04():
    num = int(input("Ingrese su numero: "))

    cant = len(str(num))

    print(f"El numero es {num} y tiene {cant} digitos")

def ejer05():
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))

    if num1 > num2:
        num1, num2 = num2, num1

    num_pair= 0
    suma = 0

    for i in range(num1+1, num2):
        print(i)

    for i in range(num1+1, num2):
        if i % 2 == 0:
            num_pair = num_pair + 1
            suma = suma + i

    print(f"\nEntre {num1} y {num2} hay {num2 - num1 + 1} digitos y {num_pair} son numeros pares.\nLa suma de los pares es: {suma}.")

def ejer06():
    num = int(input("Ingrese su numero: "))

    print(f"Tabla de multiplicar de {num}")

    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

def ejer07():
    num = int(input("Dame un numero del 1 al 19: "))

    for i in range(1,20):
        if i == num:
            continue
        print(f"{i}-- ",end="")

    print("\nTermine")

def ejer08():
    text = input("Escriba su texto: ").lower()
    word = input("Palabra que desea buscar:").lower()

    if word in text:
        print(f"La palabra {word} se encuentra en el texto")
    else:
        print("La palabra no se encuentra en el texto")

def ejer09():
    ar = int(input("Ingrese la altura del rectangulo: "))
    br = int(input("Ingrese la base del rectangulo: "))

    for i in range(ar):
        for j in range(br):
            print("*",end="")
        print("")

def ejer10():
    rut = input("Ingresa tu RUT sin puntos ni dígito verificador: ")
    serie = list(range(2,8))*2

    tur = rut[::-1]
    suma = 0

    for i in range(len(tur)):
        #suma += int(tur[i]) * serie[i]
        producto = int(tur[i]) * serie[i]
        suma = suma + producto


    modulo11 = suma % 11

    dv = 11 - modulo11

    if dv == 10:
        dv = "K"
    elif dv == 11:
        dv = 0

    print(f"Su digito verificado es {dv}")

ejer10()