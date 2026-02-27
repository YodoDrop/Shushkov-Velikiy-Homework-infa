x = []
y = []
n = len(x)
#y = b1 + b2*x
xyn = 0

for i in range(len(x)):
    xyn = xyn + x[i]*y[i]
xy = xyn/n

x2n = 0
for i in range(len(x)):
    x2n = x2n + x[i]**2
x2 = x2n/n

ymeann = 0
xmeann = 0
for i in range(n):
    xmeann = xmeann + x[i]
    ymeann = ymeann + y[i]
xmean = xmeann / n
ymean = ymeann / n

b2 = (xy-xmean*ymean)/(x2-xmean**2)

b1 = ymean - b2 * xmean

print(b1, b2)

