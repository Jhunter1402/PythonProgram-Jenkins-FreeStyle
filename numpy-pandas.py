import pandas as pd
import numpy as np

lit1 = ['A', 'B', 'C', 'D', 'E']
res1 = pd.DataFrame(lit1)
print(res1)

lit2 = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'WHITE']
indx = [101, 102, 103, 104, 105]
res2 = pd.DataFrame(lit2, index= indx)
print(res2)

lit3  = np.array(['a', 'b', 'r', 't', 'g'])
res3 = pd.DataFrame(lit3, index=['C1', 'C2', 'C3', 'C4', 'C5'])
print(res3)

dit1 = {"Name": ["JH", "Elina", "Jack"], "Age": [25, 23, 35], "Address": ["HYD", "Delhi", "HYD"]}
res4 = pd.DataFrame(dit1)
print(res4)

dit2 = data = [
    {"Name": "JH", "Age": 25, "Address": "HYD"},
    {"Name": "Elina", "Age": 23, "Address": "Delhi"},
    {"Name": "Jack", "Age": 35, "Address": "HYD"}
]
res5 = pd.DataFrame(dit2, index=[1,2,3])
print(res5)
