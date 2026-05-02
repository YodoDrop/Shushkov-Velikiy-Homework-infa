def prefix(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
                j += 1
        pi[i] = j
    return pi

def zfunc(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i-l])
        while i + z[i] < n and s[z[i]] == s[z[i]+i]:
            z[i] += 1
        if z[i] + i > r:
            l = i
            r = i + z[i]
    return z

def ztopref(z):
    n = z[0]
    pi = [0]*n
    for i in range(1, n):
        for j in range(z[i] - 1, -1, -1):
            if pi[i + j] > 0:
                break
            pi[i + j] = j + 1
    return pi






print(prefix("aabaab"))
print(zfunc("aabaab"))
print(ztopref(zfunc("aabaab")))