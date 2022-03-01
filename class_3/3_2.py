
class Point () :
    def __init__(self , x,y) :
        self.x = int(x)
        self.y = int(y)

x,y = input("Enter x1 and y1: ").split()
p1 = Point(x,y)

x,y = input("Enter x2 and y2: ").split()
p2 = Point(x,y)

d = ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
print("P1 to P2 :",d)