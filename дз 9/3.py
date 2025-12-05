import random

def QuickSort(A):
    for k in A:
        assert isinstance(k, (int, float))
    if len(A)<=1:
        return A
    else:
        b = random.choice(A)
        L = []
        M = []
        R = []
        for i in A:
            if i > b:
                L.append(i)
            elif i == b:
                M.append(i)
            else:
                R.append(i)
        return QuickSort(R)+M+QuickSort(L)


a = list(map(int, input().split()))

print(QuickSort(a))

