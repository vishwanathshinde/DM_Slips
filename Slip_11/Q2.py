import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as hc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
#
# Load the CSV file
#
df = pd.read_csv(r"C:\Users\Vishwanath\Practicals---\Data_Mining_Practicals_sem5_Pratik\DM\Assign6\Wholesale_customers_data.csv")
#
# Drop the customer id column
#
df = df.drop('Channel', axis = 1)
#
# Fill the missing values with ffill method
#
df.fillna(method ='ffill', inplace = True)
#
# Scale the data and normalize
#
sc = StandardScaler()
df_scaled = sc.fit_transform(df)
df_normalized = normalize(df_scaled)
#
# Reduce the dimensionality of data to 3 features
#
pca = PCA(n_components=6)
df_pca = pca.fit_transform(df_normalized)
df_pca = pd.DataFrame(df_pca)
df_pca.columns = ['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen']

#
# Create the Dendogram plot
#
plt.figure(figsize =(8, 8))
plt.title('Visualising the data')
dendrogram = hc.dendrogram((hc.linkage(df_pca, method ='ward')))
plt.show()