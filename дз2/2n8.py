a = list(map(int, input().split()))
def med(s):
    for i in range(len(s)):
        k1 = 0
        k2 = 0
        for j in range(len(s)):
            if s[i] >= s[j]:
                k1 += 1
            else:
                k2 += 1
        if k1-1  == k2:
            return a[i]
        else:
            continue

print(med(a))
