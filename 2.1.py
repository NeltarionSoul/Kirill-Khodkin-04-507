import random
k = int(input())
if k > 54:
    print('error')
else:
    b = random.randint(1,k)
    n = []
    S = k*(k+1) // 2
    for i in range(k):
        n.append(i+1)
    n.remove(b)
    print(n)
    for i in range(k-1):
        a = S - sum(n)
    print(a)