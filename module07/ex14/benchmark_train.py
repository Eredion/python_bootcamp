#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter as DS
from minmax import minmax

data = pd.read_csv('./space_avocado.csv')
npData = data.to_numpy()[:,1:]

mlr = MyLR(np.ones(4).reshape(-1,1), 0.000001, 100000)
mlr.fit_(npData[:,:3], npData[:,3])
print(mlr.theta)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
