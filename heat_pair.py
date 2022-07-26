import sys
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#read the file name
filename = sys.argv[1]
df = pd.read_csv(filename)
filename = filename[0:len(filename) - 3]
#add this line if you want regressions for the pair plot
p1 = sns.pairplot(df, kind = 'reg', diag_kind = 'kde', hue = 'location', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.8}})
#p1 = sns.pairplot(df, diag_kind = 'kde', hue = "location")
#creating the combination plot
(xmin, _), (_, ymax) = p1.axes[0, 0].get_position().get_points()
(_, ymin), (xmax, _) = p1.axes[-1, -1].get_position().get_points()
ax = p1.fig.add_axes([xmin, ymin, xmax - xmin, ymax - ymin], facecolor = 'none')
corr1 = df.corr()
mask1 = np.tril(np.ones_like(corr1, dtype = bool))
p2 = sns.heatmap(corr1, mask = mask1, vmin = -1, vmax = 1, cbar = False, annot = True, ax = ax)
ax.set_xticks([])
ax.set_yticks([])
#saving the plot
plt.savefig(filename + '_heat_pair.png', bbox_inches = 'tight')
