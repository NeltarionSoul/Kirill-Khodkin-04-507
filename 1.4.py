f = open('/Users/aceofspades/Documents/py №1/textfile.txt', 'r')
a = f.readlines()
k = a[1]
b = list(map(str, a[0].split()))
l = len(b)
if k=='+':
    c=0
    for i in range(l):
        c = c+int(b[i])
if k=='-':
    c=0
    for i in range(l):
        c = c-int(b[i])
if k=='*':
    c=1
    for i in range(l):
        c = c*int(b[i])
print(c)
print(b)
print(l)
    

