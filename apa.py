import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import sklearn
import csv 
import openpyxl
import xlrd
import  sqlite3
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import warnings
import _tkinter as tk
warnings.filterwarnings("ignore")

cmap=sns.diverging_palette(239,244, as_cmap=True)


a=pd.read_csv('apa.csv')
#print(a.head(7))
print(a.columns)

#renaming columns so it's easy to parse them 
col=a.rename(columns={'month': 'Month', 'Leak start':'leak_start','Leak end':'leak_end','Leak_flow':'leak_flow','Leak duration (days)':'leakduration_days'})
print (col.head(3))

#In order to understand the trends in the dashboard, I have added a separate correlation map
plt.figure(figsize=(13,7))
sns.heatmap(col.corr(), annot=True, fmt='.1f',cmap=cmap,center=0, linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
plt.show()
