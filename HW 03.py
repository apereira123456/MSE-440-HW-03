from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-440-HW-03\HW 03.csv')

X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)
        
lr = LinearRegression().fit(X, Y)

m = lr.coef_[0,0]
b = lr.intercept_[0]

x_vals = np.linspace(0,7.5, 2)
y_vals = m * x_vals + b

fig = plt.figure(dpi=300)
plt.scatter(X, Y, color='k')
plt.plot(x_vals, y_vals, label = r'$m = 0.0732 \ \Omega$/cm$^2$')
    
plt.title('ESB Cell Internal Resistance')
plt.xlabel(r'Current Density (A/cm$^2$)')
plt.ylabel(r'Cell Voltage (V)')
plt.legend()

fig.savefig('plot.png')