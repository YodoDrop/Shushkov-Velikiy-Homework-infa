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


s = input()
n = len(s)
pi = prefix(s)

cnt = [0] * (n + 1)
for i in range(n):
    cnt[pi[i]] += 1
for i in range(n, 0, -1):
    cnt[pi[i - 1]] += cnt[i]
for i in range(1, n + 1):
    cnt[i] += 1

for i in range(1, n + 1):
    print(s[:i], cnt[i])