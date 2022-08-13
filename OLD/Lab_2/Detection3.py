from aakr import AAKR
import numpy as np
from numpy.core.function_base import linspace
import pandas as pd
import matplotlib.pyplot as plt
import os
import os.path
# import glob as glob
import plotly.express as px
import re as re
# from sklearn.datasets import load_linnerud

# X = pd.read_csv('100 Sales Record.csv')

data_path = os.path.join("D:/","ChangeDetectionIdentification_input_output","General_folder","Data_out","Model1_n10000_inter10_chv5000_rep30_w100f100")

# train = pd.read_table(os.path.join(data_path,"train.dat"), sep="  ")
# test_1 = pd.read_table(os.path.join(data_path,"test_1.dat"), sep="  ")
# print(train.head)


data_in = pd.read_csv(os.path.join(data_path, "data_windows.csv"))

# data_training = data_in[data_in["CaseID"] in range(100,500)]

data_in_nc = data_in.query('CaseID >= 500 & CaseID < 4000 & Activity == 5').sort_values(by="CaseID")
data_in_obs = data_in.query('CaseID >= 4000 & CaseID <= 8000 & Activity == 5').sort_values(by="CaseID")

data_in_nc = data_in_nc.filter(items=["Waiting_time_MEAN","Processing_time_MEAN","Blocking_time_MEAN","Starving_time_MEAN"])
data_in_obs_CaseID = data_in_obs["CaseID"].tolist()
data_in_obs = data_in_obs.filter(items=["Waiting_time_MEAN","Processing_time_MEAN","Blocking_time_MEAN","Starving_time_MEAN"])


# data_in_nc = data_in_nc.to_numpy()
# data_in_obs = data_in_obs.to_numpy()

aakr_test = AAKR(bw = 1)
aakr_test.fit(data_in_nc.to_numpy())
data_in_obs_nc_transf = aakr_test.transform(data_in_obs)
data_in_obs_nc_transf = pd.DataFrame(data=data_in_obs_nc_transf,columns=data_in_obs.columns.values)
# data_in_obs_nc_transf = data_in_obs_nc_transf.insert(loc=1,column="CaseID",value=data_in_obs_CaseID,allow_duplicates=True)

colors = 'rkb'

plt.figure()
data_in_obs.plot(kind="scatter", x=linspace(4000,8000,41), y="Waiting_time")
data_in_obs_nc_transf.plot(kind="scatter", x=linspace(4000,8000,41), y="Waiting_time")
# plt.plot(data_in_obs.filter(items=["CaseID"]),data_in_obs.filter(items=["Waiting_time_MEAN"]))
# plt.plot(data_in_obs_nc_transf[:,[2]])
plt.show()

# for i in range(len(data_in_nc.index)+len(data_in_obs.index)):
#     plt.plot(data_in_nc[:, i], color=colors[i], linestyle='-',
#             label=f'Feature {i + 1} - Observed')
#     plt.plot(data_in_obs_nc_transf[:, i], color=colors[i], linestyle='--',
#             label=f'Feature {i + 1} - Normal conditions')

print(data_in_obs_CaseID)
print(data_in_obs_nc_transf)
print(linspace(4000,8000,41))
