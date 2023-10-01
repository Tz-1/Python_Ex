def ope(numbers):
    suma = sum(numbers)
    resta = numbers[0] - numbers[1] - numbers[2]
    return suma,resta

numbers = [2,4,5]

result = ope(numbers)

print(result)

