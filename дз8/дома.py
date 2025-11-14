def s(h):
    res = [0] * len(h)
    stack = []
    for i in range(len(h)):
        while stack and h[stack[-1]] < h[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        else:
            res[i] = -1
        stack.append(i)

    return res


n = list(map(int, input().split()))
print(s(n))