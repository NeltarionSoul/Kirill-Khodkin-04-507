import numpy as np
import random
a, b = random.randint(4, 10), random.randint(4, 10)
f = np.empty((a, b), dtype="object")
print(a, b)
print('\n')
def bruh(x,y):
    c = 1
    top = 0
    bot = a - 1
    left = 0
    right = b - 1
    while top <= bot and left <= right:
        for i in range(left, right + 1):
            f[top][i] = c
            c += 1
        top += 1
        for i in range(top, bot + 1):
            f[i][right] = c
            c += 1
        right -= 1
        if top <= bot:
            for i in range(right, left - 1, -1):
                f[bot][i] = c
                c += 1
            bot -= 1
        if left <= right:
            for i in range(bot, top - 1, -1):
                f[i][left] = c
                c += 1
            left += 1
    return x
    return y
bruh(a,b)
for i in f:
    for g in i:
        print(f"{g:3d}", end=" ")
    print()
print('\n')
for i in range(a):
        for g in range(b):
            f[i][g] *= i
for i in f:
    for g in i:
        print(f"{g:3d}", end=" ")
    print()