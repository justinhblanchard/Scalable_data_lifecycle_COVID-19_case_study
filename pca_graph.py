import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
#reads the file name
filename = sys.argv[1]
df = pd.read_csv(filename)
filename = filename[0:len(filename) - 3]
df1 = df.select_dtypes(include = 'object')
df = df.select_dtypes(exclude = 'object')
df = df.dropna()
#performs pca
pca = PCA(n_components = 2)
df = pca.fit_transform(df)
df = pd.DataFrame(df)
#renames the x and y axis to the amount of variance explained
df.rename({0:pca.explained_variance_ratio_[0], 1:pca.explained_variance_ratio_[1]}, axis = 1, inplace = True)
df.reset_index(drop = True, inplace = True)
df1.reset_index(drop = True, inplace = True)
df1 = pd.concat([df1, df], axis = 1)
vals = np.arange(pca.n_components_) + 1
#writes the pca values
df1.to_csv(filename + 'pca.csv', index = False)
#plots pca
sns.scatterplot(data = df1, x = pca.explained_variance_ratio_[0], y = pca.explained_variance_ratio_[1], hue = 'location', alpha = 0.3)
c = np.transpose(pca.components_[0:2, :])
print(c)
#adds the eigenvectors
for i in range(c.shape[0]):
    plt.arrow(0, 0, c[i, 0] * 3, c[i, 1] * 3)
    plt.text(c[i,0] * 3.1, c[i,1] * 3.1, i + 1, alpha = 0.5)
plt.grid()
#writes the graph
plt.savefig(filename + 'pca.png', bbox_inches = 'tight')
