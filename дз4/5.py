import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BTC_data.csv')

opn = df['open']
cls = df['close']
time = df['time']

time = np.array(time)
opn = np.array(opn)
cls = np.array(cls)

for i in range(len(time)):
    color = "red" if opn[i] > cls[i] else "green"
    plt.errorbar(time[i], (opn[i]+cls[i])/2, yerr=abs(opn[i]-cls[i])/2,color=color)

plt.show()
