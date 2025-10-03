a = input().split()
b = len(a)
c = 1
for i in range(b):
    c = c*int(a[i])
d = 1/b
print(c**d)