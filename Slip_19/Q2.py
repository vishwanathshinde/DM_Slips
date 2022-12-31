import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv(r'C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_19\data.csv')
x = df[['Weight', 'Volume']]
y = df['CO2']

model = LinearRegression().fit(x,y)
print(model.coef_)

predictedCO2 = model.predict([[2300, 1300]])
print(predictedCO2)