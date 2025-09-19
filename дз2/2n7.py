a = list(input().split())
def mult(s):
    res = 0
    num = []
    c = 0
    for i in range(len(s)):
        c1 = 0
        for l in range(len(s)):
            if s[i]==s[l]:
                c1 = c1+1
        if c1 > c:
            c = c1
            res = s[i]
    return res

print(mult(a))
