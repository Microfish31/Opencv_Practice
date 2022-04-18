import numpy as np
import os

def LoadTxtData(file_path):
    return np.loadtxt(file_path)

def FindSMD(value_array):
    lenn = len(value_array)
    #x = np.linspace(1,lenn,lenn)
    y = value_array
    dx = 1
    dydx = (abs(y[1:lenn]-y[0:lenn-1])/dx)
    summ = int(sum(dydx))
    return summ

dir_name = "data"
files = os.listdir(dir_name)

for file_name in  files :
    file_path = os.path.join(dir_name,file_name)
    get_data = LoadTxtData(file_path)
    smd = FindSMD(get_data)
    print(smd)

# ANS: g3t
# 2995
# 6559
# 3955
# 14220
# 2345
# 1839