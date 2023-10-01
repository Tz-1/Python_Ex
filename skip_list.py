data = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
dicti = {}

for i, items in enumerate(data):
    if items[0] == 0:
        continue

    if i == 0:
        dicti['A'] = items
    elif i == 1:
        dicti['B'] = items
    elif i == 2:
        dicti['C'] = [num for num in items if num != 0]
    elif i == 3:
        dicti['D'] = items

print(dicti)