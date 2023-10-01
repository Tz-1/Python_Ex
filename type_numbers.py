n = int(input("Numero: "))

if n > 0:
    print(f"{n} es positivo",end="")
elif n == 0:
    print(f"{n} es igual a cero",end="")
else:
    print(f"{n} es negativo",end="")

if n % 2 == 0:
    print(f" y es par")
else:
    print(f" y es impar")