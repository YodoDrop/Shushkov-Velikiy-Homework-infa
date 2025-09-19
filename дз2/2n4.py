l = list(map(int, input().split()))
l[0:-1:2], l[1::2]= l[1::2], l[0:-1:2]
print(l)