a = list(input().split())
def un(s):
    num = []
    for i in range(len(s)):
        c = 0
        for l in range(len(s)):
            if s[i]==s[l]:
                c = c+1
                if c > 1:
                    break
        if c == 1:
            num.append(s[i])
    return num
print(un(a))
