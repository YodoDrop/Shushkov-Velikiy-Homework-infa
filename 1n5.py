N, b, c = map(int, input().split())

l = list(map(int, str(N)[::1]))
k = 0

r = []


for i in range(0, len(l)):
    k = k + l[i]*b**(len(l)-1-i)
s = list(map(int, str(k)[::1]))

print(k, s)

while k!=0:
    r.append(k % c)
    k = k // c

print(r)

print(''.join(map(str, r[::-1])))