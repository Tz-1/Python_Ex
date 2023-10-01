lnum = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for items in lnum:
    if items[0] == 0:
        continue
    for num in items:
        if num == 0 and items.index(num) != 0:
            continue
        print(num,end=" ")

