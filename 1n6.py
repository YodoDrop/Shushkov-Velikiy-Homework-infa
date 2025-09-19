f = open('text2', 'r+')
a = f.readlines()
numbers0 =  list(map(int, a[0].split()))
op = a[1].strip()

n = int(a[2])

numbers1 = [0, 0, 0]

for j in range(0, 3):
    l = list(map(int, str(numbers0[j])[::1]))
    for i in range(0, len(l)):
        numbers1[j] = numbers1[j] + l[i]*n**(len(l)-1-i)

def back(k):
    r = []
    while k != 0:
        r.append(k % n)
        k = k // n
    return ''.join(map(str, r[::-1]))

if op == '+':
    f.write(back(numbers1[0]+numbers1[1]+numbers1[2]))
    print(back(numbers1[0]+numbers1[1]+numbers1[2]))
elif op == '*':
    f.write((back(numbers1[0]*numbers1[1]*numbers1[2])))
    print((back(numbers1[0]*numbers1[1]*numbers1[2])))
elif op == '-':
    f.write((back(numbers1[0] - numbers1[1] - numbers1[2])))
    print((back(numbers1[0] - numbers1[1] - numbers1[2])))

