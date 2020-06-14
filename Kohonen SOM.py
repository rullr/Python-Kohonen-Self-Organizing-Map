# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import random

print("@author: Muhammad Syahrul Romadhon (06111740000078)")

# Searching Function index distance minimal


def imin(m):
    a = m[0]
    index = 0
    for i in range(len(m)):
        if m[i-1] > m[i]:
            b = m[i]
            if a > b:
                index = i
    return index

# Data


A = pd.read_csv("data.csv")
print("DATA:\n", A.head(), "\n========================================================================")
# A = np.array(A)
# print(A)

# Initialization
c = 36
m = 4
n = 13
r = 0
alpha = 0.6

# weight
w = np.zeros((n, m), dtype=float)
for j in range(m):
    for i in range(n):
        w[i, j] = '{:03.1f}'.format(random.uniform(0, 1))
print("WEIGHT:\n", w, "\n=====================")

# Distance Euclidian
print("DISTANCE:")
for i in range(c):
    print("For Input vector", A.loc[i][0])
    D = np.zeros([w.shape[1]])
    for k in range(m):
        for j in range(n):
            D[k] = D[k] + (w[j, k] - A.loc[i][j+1]) ** 2
    print(D)
    index = imin(D)
    print("Winning cluster is D(", index, ")")
    print("==================================================")
    print("Update Weight (New Weight) column", index)
    for j in range(w.shape[0]):
        # print(A.loc[j][i+1])
        w[j, index] = (1-alpha)*w[j, index] + alpha*A.loc[i][j+1]
    alpha = alpha*0.5
    print(w)
    print("==================================================")
