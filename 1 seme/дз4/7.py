import string
translator = str.maketrans('', '', string.punctuation)


f = open('LICENSE.txt', 'r')


dc = f.readlines()

for i in range(len(dc)):
    dc[i] = ((dc[i].translate((translator))).strip()).lower()

s =(" ".join(dc)).split()

d = dict()

for l in s:
    if l in d:
        d[l] = d[l]+1
    else:
        d[l] = 1

dmax = dict()

for i in range(10):
    a = 0
    b = ''
    for l in d:
        if d[l]>a:
            a = d[l]
            b = l
    dmax[b] = a
    d[b] = 0
    a = 0
    b = ''
print(dmax)

