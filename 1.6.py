a = open('/Users/aceofspades/Documents/py №1/textfile-2.txt')
b = a.readlines()
a.close()
c = b[0].split()
d = b[1].strip()
e = int(b[2])

def lol(x,y):
    n=0
    strx =str(x)
    for i in range(len(strx[::-1])):
        n += int(strx[::-1][i])*y**i
    return n
def lmao(x,y):
    f = ""
    n = x
    while n > 0:
        f = (str(n%y)) + f
        n = n//y
    return f

s = lol(c[0], e)
for t in c[1:]:
    u = lol(t, e)
    if d == '+':
        s += u
    elif d == '-':
        s -= u
    elif d == '*':
        s *= u

v = lmao(s, e)
w = open('hoba.txt', 'w')
w.write(v)
w.close()