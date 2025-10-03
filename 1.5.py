def lol(x,y,z):
    n=0
    strx =str(x)
    for i in range(len(strx[::-1])):
        n += int(strx[::-1][i])*y**i
    f = ""
    while n > 0:
        f = (str(n%z)) + f
        n = n//z
    print(f) 
k = list(map(int, input().split()))
b = int(input())
c = int(input())
for i in range(len(k)):
    a = k[i]
    lol(a,b,c)