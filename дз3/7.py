import numpy as np

n = int(input()) # я не понял зачем два измерения, нам нужно n уравнений для n неизвестных
#ввод сначала x1 после x2 и тд
eq = []

for i in range(n+1):
    a = list(map(int, input().split()))
    eq.append(a)

neq = np.array(eq)

mat = np.array(neq[0:-1])

det = []

det.append(np.linalg.det(mat))

for l in range(n):
    mat[l] = neq[-1]
    det.append(np.linalg.det(mat))
    mat = neq[0:-1]

for k in range(len(det)):
    print(det[k]/det[0])





