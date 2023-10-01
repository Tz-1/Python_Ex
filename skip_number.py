"""""
n = int(input("Numero: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
"""

n = int(input("Numero: "))

for i in range(1,20):
    if i == n:
        continue
    print(f"{i}--",end="")


print(f"\nTermine. El numero saltado fue {n} ")
        
