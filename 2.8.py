import random
x = int(input())
pivo = random.sample(range(1,100), x)
print(pivo)
a = 0
b = len(pivo) // 2
if x%2 == 0:
    print('bruh')
else:
    for i in range(len(pivo)):
        for j in range(len(pivo)):
            if pivo[i] > pivo[j]:
                a += 1
        if a == b:
            print(pivo[i])
        else: a = 0
