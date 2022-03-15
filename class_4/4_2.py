
import numpy as np
from matplotlib import pyplot as plt

def FindRAngle(ni,nr,theta_i) :
    return np.arcsin(ni*np.sin(theta_i)/nr)

ni = eval(input())
nr = eval(input())
qi = eval(input()) * np.pi / 180
temp_qi = qi 

qr = FindRAngle(ni,nr,qi)
deg = qr * 180 * np.pi

theta_c = np.arcsin(nr/ni) * 180 / np.pi

if qi > theta_c :
    print(temp_qi)
else :
    print(deg)