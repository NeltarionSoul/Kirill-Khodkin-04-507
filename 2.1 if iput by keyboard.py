import random
k = list(map(int, input().split()))
if len(k) > 54:
    print('error')
else:
    b = max(k)
    c = sum(k)
    S = b*(b+1) // 2
    a = S - c
    if a == 0:
        print(b+1)
    else:
        print(a)