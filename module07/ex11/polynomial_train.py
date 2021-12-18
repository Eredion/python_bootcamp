#!/usr/bin/env python

#%%
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11).reshape(-1,1)
y = np.array([[ 1.39270298],
           [ 3.88237651],
           [ 4.37726357],
           [ 4.63389049],
           [ 7.79814439],
           [ 6.41717461],
           [ 8.63429886],
           [ 8.19939795],
           [10.37567392],
           [10.68238222]])

plt.scatter(x,y)
# %%
power = 3
x_ = add_polynomial_features(x, power)
my_lr = MyLR(np.ones(power + 1).reshape(-1,1), 0.00001, 100000)
my_lr.fit_(x_, y)

continuous_x = np.arange(1,10.01, 0.01).reshape(-1,1)
x_ = add_polynomial_features(continuous_x, power)
y_hat = my_lr.predict_(x_)

plt.scatter(x,y)
plt.plot(continuous_x, y_hat, color='orange')
plt.show()

# %%
