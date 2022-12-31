import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_12\cardata.csv')
x = df[['Weight', 'Volume']]
y = df['CO2']

model = LinearRegression().fit(x,y)

print(model.coef_)

# predict the emission of co2 of a car where a weight is 2300 and volume is 1300cm3

predictCO2 = model.predict([[2300,1300]])
print(predictCO2)