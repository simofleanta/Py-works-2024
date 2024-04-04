import csv
import pandas as pd
from pandas import DataFrame
import pandas as pd
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import datetime
import codecs
import matplotlib.pyplot as plt
 
import warnings
warnings.filterwarnings("ignore")


#Open file columns
c=pd.read_csv('freedom_index.csv')
#print(c.columns)

#Function to extract freedom_index/country

def freedom_country(f_index):
    print(f_index)
    

#freedom_country(f_index=c[c.Country=='Luxembourg'])
    
    #--------------------------------------------------Selecting data and parsing it for EU 2024 

#Creating a similar dataset with less columns so we can further process    
f=c[['Year','Country','Region','Government Integrity','Tax Burden','Fiscal Health','Property Rights','Judicial Effectiveness','Overall Score']]
#print(f)

#Taking only the 2024 dataset with less columns
fy=f[f.Year==2024]
#print(fy)

#Region EU and 2024
f_europe=fy[fy.Region=='Europe']
#print(f_europe)


#Create a pivottable to count overall scores per region for 2024
pivot1=f_europe.pivot_table(index='Overall Score',columns='Country', aggfunc={'Region':'count'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
#print(pivot1.tail(20))


#------------------------------------------------------graphs 

sns.violinplot(x=fy["Region"], y=fy["Overall Score"], palette="Blues")
#plt.show()


plt.figure(figsize=(10,7))
sns.heatmap(f_europe.corr(), annot=True, cmap=sns.diverging_palette(100,200, as_cmap=True),center=0, linewidth=1,vmin=-1,vmax=1, yticklabels=True,xticklabels=True)
#plt.show()

plt.figure(figsize=(13,7))
sns.countplot(data=fy,x='Region',color='darkblue',order=fy)
plt.xticks(rotation=45)
#plt.show()



