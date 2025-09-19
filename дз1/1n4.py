from os import write

f = open("text", "r+")
n = list(map(float, f.readline().split()))
t = f.readlines()
k = t[0]
if k == '+':
    print(n[1]+n[0])
    f.write(str(n[1]+n[0]))
elif k == '-':
    print(n[1]-n[0])
    f.write(str(n[1] - n[0]))
elif k == '*':
    print(n[1]*n[0])
    f.write(str(n[1] * n[0]))







