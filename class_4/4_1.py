import math
import numpy as np
from matplotlib import pyplot as plt

def FindRAngle(ni,nr,theta_i) :
    return np.arcsin(ni*np.sin(theta_i)/nr)

ni = 1
nr = 1.5

angle = np.linspace(0,90,100)
theta_i = angle*math.pi/180
theta_r = FindRAngle(ni,nr,theta_i)

theta_p = theta_i - theta_r
t = 5
d = t/np.cos(theta_r)  * np.sin(theta_p)

 # 畫圖
plt.plot(angle,d)
plt.grid()
plt.show()
