import numpy as np
n = int(input())
m = n + 1
matrix = []
for i in range(n):
    n = []
    for g in range(m):
        a = float(input([{i+1},{g+1}]))
        n.append(a)
    matrix.append(n)
A = []
B = []
for i in range(n):
    B.append(matrix[i][m])
print(B)
print(np.array(matrix))