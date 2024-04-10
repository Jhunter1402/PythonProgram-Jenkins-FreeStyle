import pandas as pd
import numpy as np

lit1 = ['A', 'B', 'C', 'D', 'E']
res1 = pd.Series(lit1)
print(res1)
print(type(res1  ))

lit2 = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'WHITE']
indx = [101, 102, 103, 104, 105]
res2 = pd.Series(lit2, index= indx)
print(res2)

lit3  = np.array(['a', 'b', 'r', 't', 'g'])
res3 = pd.Series(lit3, index=['C1', 'C2', 'C3', 'C4', 'C5'])
print(res3)

dit = {"Name": "JH", "Age": 25, "Address": "HYD" }
res4 = pd.Series(dit)
print(res4)