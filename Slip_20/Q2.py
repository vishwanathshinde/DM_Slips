import pandas as pd
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch

dataset = pd.read_csv(r'C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_20\Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values
dendrogram = sch.dendrogram(sch.linkage(X,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()