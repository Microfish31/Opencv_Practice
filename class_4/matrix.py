import numpy as np

def D(num):
    return np.array([[1,num],
                     [0,1]
                    ])

def L(num):
    return np.array([[1,0],
                     [-1/num,1]
                    ])

def Light(h,a) :
    return np.array([[h],
                     [a]
                   ])

h = 0
a = float(input())

# use loop or if maybe better
get = D(150).dot(L(80))
get = get.dot(D(220))
get = get.dot(L(100))
get = get.dot(D(120))
get = get.dot(Light(h,a))
print(get)
