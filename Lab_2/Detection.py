import numpy as np

from aakr import AAKR

from sklearn.datasets import load_linnerud

X = load_linnerud().data
print(X)
X_nc = X[:15]
X_obs = X[15:]

aakr = AAKR()
aakr.fit(X_nc)
X_obs_nc = aakr.transform(X_obs)

import matplotlib.pyplot as plt

colors = 'rkb'
for i in range(X.shape[1]):
    plt.plot(X_obs[:, i], color=colors[i], linestyle='-',
            label=f'Feature {i + 1} - Observed')
    plt.plot(X_obs_nc[:, i], color=colors[i], linestyle='--',
            label=f'Feature {i + 1} - Normal conditions')

plt.title('Observed and normal conditions for Linnerud dataset')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
