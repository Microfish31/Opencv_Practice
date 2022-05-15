import time
import numpy as np
import matplotlib.pyplot as plt 

x=np.linspace(-10,10,50)
T=np.linspace(-10,10,50)
Y=np.zeros(len(T))
dx=(10--10)/50

for i in range(0,len(T)) :
    t=T[i]
    y0=np.exp(-(t-x)**2)
    y0[np.where(y0>0.01)] = 1
    y0[np.where(y0<=0.01)] = 0
    y1=np.exp(-(x-2)**2)
    y2=np.exp(-(x+2)**2)
    Y[i]=np.sum(y2*y1*y0)*dx
    
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(x,y0,x,y1,x,y2)
    plt.axis([-10,10,0,3])

    plt.subplot(2,1,2)
    plt.plot(x[i],Y[i],'o')
    plt.axis([-10,10,0,3])
    plt.show()

plt.figure(2)
plt.plot(x,y1/max(y1),x,Y/max(Y))
plt.show()