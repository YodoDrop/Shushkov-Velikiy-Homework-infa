import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import count

df = pd.read_csv('iris_data.csv')


species = df['Species'].unique()

plt.pie([list(df['Species']).count(i) for i in species], labels = species)

plt.show()