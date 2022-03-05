from matplotlib import pyplot as plt
from numpy import linspace

class Point () :
    def __init__(self , x, y) :
        self.x = float(x)
        self.y = float(y)

class Vector () :
    def __init__(self , x, y) :
        self.x = float(x)
        self.y = float(y)

def Fun(x) :
    return x**0.5

def Defun(y) :
    return y**2

def Limfun(x):
    return 0.5*(x**(-0.5))

if __name__ == '__main__' :
   height = [0.01,0.05,0.1]
   xl_max = 1
   yl_max = 0.5

   x = linspace(0,xl_max,500)
   y = x**0.5
   
   a_vec = Vector(-1,0)

   for yy in height :
      p = Point(Defun(yy),yy)
      m = Limfun(p.x)
      n_vec = Vector(1,(-1/m))
      b_vec = Vector(-1,-1)
      b_constant = a_vec.x * n_vec.x + a_vec.y * n_vec.y
      b_vec = Vector(b_constant*n_vec.x,b_constant*n_vec.y)
      c_vec = Vector(a_vec.x-2*b_vec.x,a_vec.y-2*b_vec.y)
      
      m_r = c_vec.y/c_vec.x
      r_line = m_r * (x-p.x) + p.y

      plt.plot([p.x,xl_max],[yy,yy])
      plt.plot(x,r_line)

   plt.plot(x,y,x,-1*y)
   plt.xlim([-0.2,xl_max]) 
   plt.ylim([-1*yl_max,yl_max]) 
   plt.show()