import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
x=np.array([1,2,3,4,5,6,7,8])
x=np.array(x).reshape((-1,1))
y=np.array([7,14,15,18,19,21,26,23])
model=LinearRegression().fit(x,y)
print(f"intercept b0:{model.intercept_}")
print(f"slope b1:{model.coef_}")

def myfunc(x):
    return model.coef_ * x + model.intercept_

plt.scatter(x,y)
plt.scatter(x,list(map(myfunc , x)))
plt.show()