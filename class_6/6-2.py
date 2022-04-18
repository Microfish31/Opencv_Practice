import numpy as np
import matplotlib.pyplot as plt 

def FindFES(areas) :
    X1 = areas[0]+areas[2]
    X2 = areas[1]+areas[3]
    return ( X1 - X2 ) / ( X1 + X2 )

def whichArea(a,b,x,y) :
    m = (x**2)/(a**2) + (y**2) / (b**2)
    if m <= 1 :
        if (x+y)>0 and (x-y)<0 :
            return 0
        elif (x-y)>0 and (x+y) > 0:
            return 1
        elif (x+y)<0 and (x-y)>0 :
            return 2
        elif (x-y) < 0 and (x+y) < 0:
            return 3
    return -1

N = 100
ss = np.linspace(0,100,100)
areas = [0,0,0,0]
fes = []

for s in ss :
    a = 10 + 10*s/100
    b = 20 - 10*s/100

    dA = (2*a/N) * (2*b/N)
    xx = np.linspace(-1*a,a,N)
    yy = np.linspace(-1*b,b,N)

    for x in xx:
        for y in yy :
            area_index = whichArea(a,b,x,y)
            if area_index != -1 :
                areas[area_index] += dA
                
    fes.append(FindFES(areas))

plt.plot(ss,fes,'-')
plt.show()
   