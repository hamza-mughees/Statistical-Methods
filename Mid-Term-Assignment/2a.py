import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv', header=None)

# column on which E[Z_i1] is conditioned (0-indexed)
conditioned_on = 1

# looping through the possible values of z
for z in set(df[conditioned_on]):
    # obtaining set of baskets where Z_i,2 = z
    baskets = df.loc[df[conditioned_on] == z]
    # getting size of this set
    N = len(baskets)
    # getting number of baskets which contain item 1
    b = sum(baskets[0])
    # calculating sample mean
    sample_mean = b / N
    print(f'For z = {z}: N = {N}, b = {b}, sample mean = {sample_mean}')
