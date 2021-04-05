import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv', header=None)

def clt_95(N, variance):
    return 2*((variance/N)**0.5)

def chebyshev_95(N, variance):
    return (variance/(0.05*N))**0.5

def print_confidence_interval(sample_mean, bound_offset):
    print(f'{sample_mean-bound_offset} <= X <= {sample_mean+bound_offset}')

conditioned_on = 1

for z in set(df[conditioned_on]):
    baskets = df.loc[df[conditioned_on] == z]
    N = len(baskets)
    b = sum(baskets[0])
    sample_mean = b / N
    # calculating variance
    variance = sample_mean*(1-sample_mean)
    # clt error bound
    clt = clt_95(N, variance)
    # chebyshev error bound
    chebyshev = chebyshev_95(N, variance)

    print(f'For z = {z}:\nCLT:')
    print_confidence_interval(sample_mean, clt)
    print('Chebyshev:')
    print_confidence_interval(sample_mean, chebyshev)
    print()
