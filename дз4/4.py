import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import count
import scipy as sp

from numpy.ma.extras import polyfit

df = pd.read_csv('iris_data.csv')

print(type(df))

sl = df['SepalLengthCm']
sw = df['SepalWidthCm']
pl = df['PetalLengthCm']
pw = df['PetalWidthCm']



fig, ax = plt.subplots(3, 2)
ax[0, 0].scatter(sl, sw)
ax[1, 0].scatter(sl, pl)
ax[2, 0].scatter(sl, pw)
ax[0, 1].scatter(sw, pl)
ax[1, 1].scatter(sw, pw)

a = np.polyfit(pl, pw, 1)


ax[2,1].plot([1, 6], [a[1]+a[0], 6*a[0]+a[1]], 'r')
ax[2,1].scatter(pl, pw)
ax[2,1].set_title('PetalLengthCm, PetalWidthCm')




plt.show()




