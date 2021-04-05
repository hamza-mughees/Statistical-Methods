import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 'data.csv' containing baskets and items
df = pd.read_csv('./data.csv', header=None)

# summing each row to get number of items in each basket
x = df.sum(axis=1)
# changing from frequencies to probabilities
weights = np.ones_like(x) / len(x)

# plotting the histogram
plt.hist(x, weights=weights, edgecolor='black')
plt.show()
