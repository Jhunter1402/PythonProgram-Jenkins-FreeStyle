import pandas as pd

data1 = {"Name": ["JH", "Elina", "Jack"], "Age": [25, 23, 35], "Address": ["HYD", "Delhi", "HYD"]}
df1 = pd.DataFrame(data1)
print(df1)
print(df1[['Name', 'Address']])

data2= pd.read_csv("data.csv")
print(data2)
print(data2.loc[1:3])
