import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv(r'C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_10\iris_csv.csv');

store_data.head()

records = []

for i in range(0,151):
    records.append([str(store_data.values[i,j]) for j in range(0,20)])

association_rules = apriori(records, min_support = 0.045, min_confidence = 0.2, min_lift = 3, min_length = 2)

association_results = list(association_rules)

print(len(association_results))