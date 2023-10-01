def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multip(a,b):
    return a*b

def divid(a,b):
    return a/b

def ope(a,b):
    suma = sumar(a,b)
    resta = restar(a,b)
    multi = multip(a,b)
    divi = divid(a,b)
    dicc = {"Suma": suma, "Resta": resta, "Multiplicación": multi, "División": divi}
    return dicc

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

result = ope(a,b)
print(result)