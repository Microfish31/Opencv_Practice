# problem
import numpy as np
import matplotlib.pyplot as plt

p = ['A','B','C','D','E']
x = [1,2,3,4,5]
y = [1,2,3,4,8]

Q = np.linspace(-np.pi/2,np.pi/2,500)
R = np.linspace(-10,10,500)

dR = (max(R)-min(R))/len(R)

r = [0,0,0,0,0]
c = ['A','B','C','D','E']

for q in Q:
    for i in range(5):
        r[i] = x[i]*np.cos(q)+y[i]*np.sin(q)
  
    box = []
    for rr in R :
        if r[0]>rr and r[0]<rr+dR :
            box.append(c[0])
        if r[1]>rr and r[1]<rr+dR :
            box.append(c[1])
        if r[2]>rr and r[2]<rr+dR :
            box.append(c[2])
        if r[3]>rr and r[3]<rr+dR :
            box.append(c[3])
        if r[4]>rr and r[4]<rr+dR :
            box.append(c[4])
    
        if len(box) > 3 :
            print(box)
        else :
            box = []
    box = []