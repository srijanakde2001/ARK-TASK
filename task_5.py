import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = pd.read_excel('C:/Users/saume/Downloads/radar_dump.xlsx')
data = data.fillna(value = 0)
print(data)
