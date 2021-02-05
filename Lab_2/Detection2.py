from aakr import AAKR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import plotly.express as px
# from sklearn.datasets import load_linnerud

# X = pd.read_csv('100 Sales Record.csv')

data_path = os.path.join("D:/","ChangeDetectionIdentification_input_output","General_folder","Data_out","Model1_n10000_inter10_chv5000_rep30_w100f100")

# print(data_path)

data_in = pd.read_csv(os.path.join(data_path,"data_out_standard.csv"))

data_in_plot = data_in[data_in["Activity"]==5]

# print(pd.DataFrame(data_in_plot).dtypes)

plot_plotly = px.scatter(data_in_plot, x="CaseID", y="Processing_time")
plot_plotly.show()
print(data_in)

# X_nc = X[:15]
# X_obs = X[15:]

# aakr = AAKR()
# aakr.fit(X_nc)
# X_obs_nc = aakr.transform(X_obs)

# import matplotlib.pyplot as plt

# colors = 'rkb'
# for i in range(X.shape[1]):
#     plt.plot(X_obs[:, i], color=colors[i], linestyle='-',
#             label=f'Feature {i + 1} - Observed')
#     plt.plot(X_obs_nc[:, i], color=colors[i], linestyle='--',
#             label=f'Feature {i + 1} - Normal conditions')

# plt.title('Observed and normal conditions for Linnerud dataset')
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
