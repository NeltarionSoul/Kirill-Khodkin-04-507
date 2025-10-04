import numpy as np
def kukold(x,y):
    if len(x) != len(y):
        print('peredelivay')
    else:
        zxc = (len(x)*sum(x*y) - sum(x)*sum(y)) / (len(x)*sum(x**2) - sum(x)**2)
        print(zxc)
        qwe = sum(y) / len(y) - zxc * sum(x) / len(x)
        print(qwe)
z = list(map(int, input().split()))
c = list(map(int, input().split()))
r = np.array(z)
t = np.array(c)
kukold(r,t)