
"""
lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

del lista[3]
del lista[5]
del lista[5]
del lista[6]
lista.sort()

print(lista)
"""

"""
var1 = ["da","va","ba"]

var2 = var1 [:] #Separa en dos listas iguales modificables
"""

lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]
new_list = []

for i in lista:
    if i not in new_list:
        new_list.append(i)
lista = new_list

lista.sort()

print(lista)

