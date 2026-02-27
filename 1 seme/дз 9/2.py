x = []
y = []
n = len(x)

assert len(x) == len(y), "Массивы x и y должны иметь одинаковую длину"
assert n > 1, "Необходимо как минимум 2 точки данных для расчета регрессии"

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

assert (x2 - xmean**2) != 0, "Дисперсия x не должна быть равна нулю (все x одинаковы)"

b2 = (xy-xmean*ymean)/(x2-xmean**2)

b1 = ymean - b2 * xmean

assert isinstance(b1, (int, float)), "Коэффициент b1 должен быть числом"
assert isinstance(b2, (int, float)), "Коэффициент b2 должен быть числом"

calculated_y_mean = b1 + b2 * xmean
assert abs(ymean - calculated_y_mean) < 1e-10, f"Ошибка в расчетах: средняя точка не лежит на линии регрессии"

print(b1, b2)