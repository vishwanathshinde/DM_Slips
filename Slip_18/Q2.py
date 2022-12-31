import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5,6,7,8])
x = np.array(x).reshape(-1,1)
y = np.array([7,14,15,18,19,21,26,23])

model = LinearRegression().fit(x,y)

print(model.intercept_)
print(model.coef_)

def mymodel(x):
    return model.coef_ * x + model.intercept_

plt.scatter(x,y)
plt.scatter(x,list(map(mymodel,x)))
plt.show()