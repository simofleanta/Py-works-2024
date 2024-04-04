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

#since I am a blood donor I wanted to see blood types distributons across countries  
#data from kaggle

#open files 
bo=pd.read_csv('bloodtypes.csv')
#print(bo.head(10)) #first
print(bo.tail(40)) #last 
print(bo[22:74]) # from 22 line :74


#Bloodtype for one country 
Dinamarca=bo[bo.Country=='Dinamarca'] 
#print(Dinamarca) 

#A function that exxtracts blood type per country
def bloodtype(blood_fn):
    print(blood_fn)
    

bloodtype(blood_fn=bo[bo.Country=='Dinamarca'])

#############################################################

# just for curiosity i analyzed salaries accross jobs and experience levels 
 #Print columns of the file   
df=pd.read_csv('ds_salaries.csv')
print(df)
print(df.columns)

#Print selected columns 
df_columns=df[['salary','company_location']]
#print(df_columns)

##################################################################################

#After taking my heritage dna results I wanted to see where my dna matches mostly live 


# Decoding UTF - 8 FILE ON my heritage dna match 

#Open file
c='cluster.csv'

#decode 
utf_cluster=pd.read_csv(c, encoding=('ISO-8859-1'), low_memory=False)

#Print file
print(utf_cluster.head(5))


####################################################

#Data filter
#utf-8 decoding
#violin plot
#Function extracting countries per cluster 
#data aggregation and pivotation 




                             #EDA ON DNA MATCH 

#Open and filter per country 


# DNA Matches in Germany
DE=df[df.Country=='Germany']
#print(DE)


#####################################################################

#Function extracting countries per cluster 

df=pd.read_csv('clusters.csv')
print(df)

def countries(percluster):
    print(percluster)
    

countries(percluster=df[df.Cluster=='Western Europe'])



#Violin plots

sns.violinplot(x=df["Cluster"], y=df["Percent DNA shared"], palette="Blues")
#plt.show()

#Aggregation and grouping 
x=df.groupby(['Cluster'])[['Age']]
print(x.count())

Fin=df[df.Country=='Finland']
print(Fin)

#agregate by age in finland

F=Fin.groupby(['Age'])[['Total cM shared']]
print(F.count())

 #pivot

pivot1=DE.pivot_table(index='Total cM shared',columns='Cluster', aggfunc={'Age':'count'}).fillna(0)
pivot1['Max']=pivot1.idxmax(axis=1)
print(pivot1.head(60))
