def fac(n,k=2,r=[]):
    assert (n > 0 and isinstance(n, int)), 'n is expected to be a pos int'
    if n==1:
        return r
    if n%k==0:
        return fac(n//k,k,r+[k])
    else:
        return fac(n,k+1,r)


a, b = map(int, input().split())


dlist = []

al = fac(a)
bl = fac(b)


for i in range(len(fac(a))):
    if al[i] in bl:
        dlist.append(al[i])
        bl.remove(al[i])

d = 1
for i in dlist:
    d = d*i


y1 = 0

while (d-y1*b)/a%1!=0:
    y1 = y1 +1

x1 = 0
while (d-x1*a)/b%1!=0:
    x1 = x1 +1

if y1**2+((d-y1*b)/a)**2 > x1**2+((d-x1*a)/b)**2:
    print(x1, int((d-x1*a)/b), d)
elif y1**2+((d-y1*b)/a)**2 < x1**2+((d-x1*a)/b)**2:
    print(int((d-y1*b)/a), y1,  d)
elif y1**2+((d-y1*b)/a)**2 == x1**2+((d-x1*a)/b)**2:
    if x1 <= y1:
        print(x1, int((d - x1 * a) / b), d)
    else:
        print(int((d - y1 * b) / a),y1,  d)





