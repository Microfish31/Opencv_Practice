import matplotlib.pyplot as plt
import numpy as np

class Point () :
    def __init__(self ,x,y,z) :
        self.x = x
        self.y = y
        self.z = z

x = np.linspace(-30,30,500)
X,Y = np.meshgrid(x,x)
z = 5
L = 0.5
c1 = Point(1,0,z)
c2 = Point(0,-1,z)
r1 = np.sqrt((c1.x-X)**2+(c1.y-Y)**2+c1.z**2)
r2 = np.sqrt((c2.x-X)**2+(c2.y-Y)**2+c2.z**2)
k = 2*np.pi/L
E1 = np.exp(1j*k*r1)
E2 = np.exp(1j*k*r2)
I = abs(E1+E2)**2
plt.imshow(I,cmap='gray')
plt.show()
