import numpy as np
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    n = []
    for g in range(m):
        a = float(input([{i+1},{g+1}]))
        n.append(a)
    matrix.append(n)
print(np.array(matrix))