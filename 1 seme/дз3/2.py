def fac(n,k=2,r=[]):
    if n==1:
        return r
    if n%k==0:
        return fac(n//k,k,r+[k])
    else:
        return fac(n,k+1,r)

x = int(input())

print(fac(x))

