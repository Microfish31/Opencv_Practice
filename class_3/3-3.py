class Eq () :
    def __init__(self , a, b, c ) :
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

a,b,c = input("Enter a1,b1,c1 :").split()
E1 = Eq(a,b,c)

a,b,c = input("Enter a2,b2,c2 :").split()
E2 = Eq(a,b,c)

delta = (E1.a * E2.b) - (E1.b * E2.a)
delta_x = (E1.c * E2.b) - (E1.b * E2.c)
delta_y = (E1.a * E2.c) - (E1.c * E2.a)

print("node = ( " + str(delta_x/delta) + " , " + str(delta_y/delta) + " )")