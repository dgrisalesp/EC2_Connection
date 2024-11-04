import sys
import os
import pandas as pd
sys.stdout=open('output.txt','w')
data=[
    {'name':'John','age':25,'salary':50000},
    {'name':'Jane','age':30,'salary':60000},
    {'name':'James','age':27,'salary':70000}
]
dataframe=pd.DataFrame(data)
print(dataframe)
print(type(dataframe))
print(dataframe.shape)