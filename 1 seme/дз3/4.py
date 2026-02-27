from math import copysign, floor

size = int(input())
symb = input()
c = 0

if size%2==0:
    for i in range(size//2+1):
        print(symb*i)
    for i in range(size//2,0,-1):
        print(symb * i)
else:
    for i in range(-int(floor(size / 2)), int(floor(size / 2) + 1)):
        c = int(c - copysign(1, i - 1))
        print(symb * c)






