from itertools import count

with open('text2n9', 'r') as f:
    t = "".join(f.readlines())

l = ['.', '!', '?']
c = 0
for i in range(len(t)-1):
    if t[i+1] in l and t[i] not in l:
        c = c +1
print(c)
