import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
filename = sys.argv[1]
df = pd.read_csv(filename)
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
kmeans = KMeans(n_clusters = 4, random_state = 0).fit(df)
sns.scatterplot(data = df, x = df.columns[0], y = df.columns[1], hue = kmeans.labels_ + 1)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker= "X", label = "centroids")
plt.legend()
plt.savefig(filename + '.png', bbox_inches = 'tight')