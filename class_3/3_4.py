from matplotlib import pyplot as plt
from numpy import linspace
import math

class Point () :
    def __init__(self , x, y) :
        self.x = float(x)
        self.y = float(y)

class Eq () :
    def __init__(self , a, b, c ) :
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

def FindNode(E1,E2) :
    delta = (E1.a * E2.b) - (E1.b * E2.a)
    delta_x = (E1.c * E2.b) - (E1.b * E2.c)
    delta_y = (E1.a * E2.c) - (E1.c * E2.a)
    node = Point(delta_x/delta,delta_y/delta)
    print((node.x,node.y))
    return node

def FindSlope(P1,P2) :
    return (P2.y - P1.y)/(P2.x-P1.x)

if __name__ == '__main__' :
    # 建立點
    p_start = Point(-1,2)
    p_m = Point(-2,0)
    p_n = Point(0,1)

    # 找斜率
    m1 = FindSlope(p_start,p_m)
    m2 = FindSlope(p_start,p_n)

    # 反射斜率計算
    M_m = p_start.y/p_start.x
    m1_r_x = 1 - 2 * (1)
    m1_r_y = m1 - 2 * (M_m*m1)
    m1_r = m1_r_y / m1_r_x

    m2_r_x = 1 - 2 * (1)
    m2_r_y = m2 - 2 * (M_m*m2)
    m2_r = m2_r_y / m2_r_x

    # 切多份為點陣列 (x)，以原點為基礎位移構成方程式
    x = linspace(-3,3,100)
    y1 = m1_r * (x-p_m.x) + p_m.y
    y2 = m2_r * (x-p_n.x) + p_n.y
    M = 0.5*x + 1

    # 計算交點
    E1 = Eq(-1*m1_r,1,(p_m.y-m1_r*p_m.x))
    E2 = Eq(-1*m2_r,1,(p_n.y-m2_r*p_n.x))
    node = FindNode(E1,E2)

    # 畫圖
    plt.plot(x,y1,x,y2,x,M)

    plt.plot([p_start.x,p_m.x],[p_start.y,p_m.y],'-',c='blue')
    plt.plot([p_start.x,p_n.x],[p_start.y,p_n.y],'-',c='purple')
    plt.hlines(0,-3,3,color="green")
    plt.scatter([p_n.x,p_m.x,p_start.x,0], [p_n.y,p_m.y,p_start.y,0], s=25, c='b')
    plt.scatter([0], [0], s=25, c='g')
    plt.scatter([node.x], [node.y], s=25, c='r')    

    plt.grid()
    plt.show()