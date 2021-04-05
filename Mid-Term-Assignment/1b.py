import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv', header=None)

# obtaining first column (i.e. frequency of first item in each 
# basket)
x = df[0]
# obtaining number of baskets
N = len(x)

# calculating probability
probability = sum(x) / N
print(f'N = {N}')
print(f'probability = {probability}')
