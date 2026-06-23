import pandas as pd
data={'name':['asha','ravi','john'],'age':[22,25,23]}
df=pd.DataFrame(data)
print(df)
s=pd.Series([1,2,3])
print(s)
r=pd.Series([1,2,3],index=['a','b','c'])
print(r)