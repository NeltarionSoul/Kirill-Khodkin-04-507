import random
k = list(map(int, input().split()))
l = len(k)
if l > 54:
    print('error')
else:
    c = sum(k)
    S = (l+1)*(l+2) // 2
    a = S - c
    if a == 0:
        print(l+1)
    else:
        print(a)
# A = list(map(int, input().split()))
# print(A[0]*(A[0]+1//2 - (sum(A) - A[0]))