import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,300)
a = 10
b = 15
X,Y = np.meshgrid(x,x)
Z1 = np.sin(25*(X**2/a+Y**2/b))
Z2 = np.sin(25*(X**2/a-Y**2/b))
plt.figure(1)
plt.imshow(Z1,cmap='Reds')
plt.figure(2)
plt.imshow(Z2,cmap='Reds')
plt.show()