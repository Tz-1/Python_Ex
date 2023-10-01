"""
n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Tercer numero: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
    if n2 >= n3:
        middle = n2
        smallest = n3
    else:
        middle = n3
        smallest = n2

elif n2 >= n1 and n2 >= n3:
    largest = n2
    if n1 >= n3:
        middle = n1
        smallest = n3
    else:
        middle = n3
        smallest = n1
else:
    largest = n3
    if n1 >= n2:
        middle = n1
        smallest = n2
    else:
        middle = n2
        smallest = n1

print(f"Los numero de mayor a menor son: {largest}, {middle}, {smallest}")
"""

n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Tercer numero: "))

numeros = [n1, n2, n3]

numeros.sort(reverse=True)

print(f"Los numero de mayor a menor son: {numeros}")