import matplotlib.pyplot as plt
import statistics as st
from scipy import stats
from scipy.stats import norm
import numpy as np

with open(r"data.txt", "r", encoding='utf-8') as f:
    a = str(f.read()).split()
    b = list(map(int,a))


    w1 = {}
    sum101 = []
    for i in range(1,4000,10):
        w1[i] = 0
    for i in range(1,4000,10):
        sum101.append(sum(b[0+i:9+i]))
    sm101d = {}
    for i in sum101:
        sm101d[i] = 0
    for i in sum101:
        sm101d[i] += 1
    nsm101d = {key: value/400 for key, value in sm101d.items()}
    keys1 = nsm101d.keys()
    values1 = nsm101d.values()

nmean1 = st.mean(sum101)
sdev1 = st.stdev(sum101)
sem1 = stats.sem(sum101)
aps1 = nmean1/4000
semaps1 = sem1/4000


figure, axis = plt.subplots(2, 2)

x1 = np.linspace(nmean1-3*sdev1, nmean1+3*sdev1, 1000)
y1 = norm(loc=nmean1, scale=sdev1).pdf(x1)

axis[0,0].plot(x1,y1, 'r')
axis[0,0].text(15, 0.11, r'$\tau$ = 10c'f'\nn = {nmean1}',
         fontsize=7, color='black', bbox=dict(boxstyle='round', facecolor='green', alpha=0.7))
axis[0,0].bar(keys1,values1)


csem1 = 0
csem2 = 0
csem3 = 0

for i in range(len(sum101)):
    if abs(nmean1-sum101[i])<sdev1:
        csem1 = csem1 + 1
    if abs(nmean1-sum101[i])<2*sdev1:
        csem2 = csem2 + 1
    if abs(nmean1-sum101[i])<3*sdev1:
        csem3 = csem3 + 1






w2 = {}
sum102 = []
for i in range(1,4000,20):
    w2[i] = 0
for i in range(1,4000,20):
    sum102.append(sum(b[0+i:19+i]))
sm102d = {}
for i in sum102:
    sm102d[i] = 0
for i in sum102:
    sm102d[i] += 1
nsm102d = {key: value/200 for key, value in sm102d.items()}
keys2 = nsm102d.keys()
values2 = nsm102d.values()


nmean2 = st.mean(sum102)
sdev2 = st.stdev(sum102)
sem2 = stats.sem(sum102)
aps2 = nmean2/4000
semaps2 = sem2/4000


x2 = np.linspace(nmean2-3*sdev2, nmean2+3*sdev2, 1000)
y2 = norm(loc=nmean2, scale=sdev2).pdf(x2)

axis[0,1].plot(x2,y2, 'r')
axis[0,1].text(25, 0.085, r'$\tau$ = 20c'f'\nn = {nmean2}',
         fontsize=7, color='black', bbox=dict(boxstyle='round', facecolor='green', alpha=0.7))
axis[0,1].bar(keys2,values2)

csem1 = 0
csem2 = 0
csem3 = 0

for i in range(len(sum102)):
    if abs(nmean2-sum102[i])<sdev2:
        csem1 = csem1 + 1
    if abs(nmean2-sum102[i])<2*sdev2:
        csem2 = csem2 + 1
    if abs(nmean1-sum101[i])<3*sdev2:
        csem3 = csem3 + 1

print(csem1/200, csem2/200, csem3/200, sdev2)



w3 = {}
sum103 = []
for i in range(1,4000,40):
    w3[i] = 0
for i in range(1,4000,40):
    sum103.append(sum(b[0+i:39+i]))
sm103d = {}
for i in sum103:
    sm103d[i] = 0
for i in sum103:
    sm103d[i] += 1
nsm103d = {key: value/100 for key, value in sm103d.items()}
keys3 = nsm103d.keys()
values3 = nsm103d.values()


nmean3 = st.mean(sum103)
sdev3 = st.stdev(sum103)
sem3 = stats.sem(sum103)
aps3 = nmean3/4000
semaps3 = sem3/4000


x3 = np.linspace(nmean3-3*sdev3, nmean3+3*sdev3, 1000)
y3 = norm(loc=nmean3, scale=sdev3).pdf(x3)

axis[1,0].plot(x3,y3, 'r')
axis[1,0].text(25, 0.085, r'$\tau$ = 40c'f'\nn = {nmean3}',
         fontsize=7, color='black', bbox=dict(boxstyle='round', facecolor='green', alpha=0.7))
axis[1,0].bar(keys3,values3)



w4 = {}
sum104 = []
for i in range(1,4000,80):
    w4[i] = 0
for i in range(1,4000,80):
    sum104.append(sum(b[0+i:79+i]))
sm104d = {}
for i in sum104:
    sm104d[i] = 0
for i in sum104:
    sm104d[i] += 1
nsm104d = {key: value/800 for key, value in sm104d.items()}
keys4 = nsm104d.keys()
values4 = nsm104d.values()


nmean4 = st.mean(sum104)
sdev4 = st.stdev(sum104)
sem4 = stats.sem(sum104)
aps4 = nmean4/4000
semaps4 = sem4/4000


x4 = np.linspace(nmean4-3*sdev4, nmean4+3*sdev4, 1000)
y4 = norm(loc=nmean4, scale=sdev4).pdf(x4)

#axis[1,1].plot(x4,y4, 'r')
axis[1,1].text(85, 0.006, r'$\tau$ = 80c'f'\nn = {nmean4}',
         fontsize=7, color='black', bbox=dict(boxstyle='round', facecolor='green', alpha=0.7))
axis[1,1].bar(keys4,values4)


print(round(nmean4, 2),"&", round(sdev4, 2),"&", round(sem4, 2),"&", round(aps4,3),"&", semaps4)

plt.show()