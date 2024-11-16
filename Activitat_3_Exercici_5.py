num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
sumaParells = 0
sumaSenars = 0
for i in num:
    if i%2 == 0:
        print(f"{i} és parell.")
        sumaParells += i
    else:
        print(f"{i} és senar.")
        sumaSenars += i
print(f"La suma dels parells és {sumaParells} i la dels senars és {sumaSenars}")