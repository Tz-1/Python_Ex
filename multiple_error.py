#except can be used with different parameters in the same sentences
#if you don't use a type of erro then you should leave the except blank (If blank always last)

contador = 0
calculo_suma = 0
print("Sumatoria de 4 numero enteros")
while contador < 4:
    try:
        valor = int(input(f'Ingrese el numero entero {contador+1}: '))
        calculo_suma += valor
        contador +=1
    except:
        print("Valor Errado: Ingrese un numero correcto")
    else:
        print("No se capturaron excepciones, todo bien")
    finally:
        print("Finally se ejecuta al final de la ejecución con o sin excepciones")

print("El resultado de la suma es: ", calculo_suma)