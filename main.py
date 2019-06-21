import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

data = pd.read_csv("train.csv").head(100)

plt.figure(figsize=(10,6), dpi=80)
plt.plot(data["Id"],data["LotArea"])
plt.scatter(data["Id"],data["LotArea"])
plt.show()
# print(data)

