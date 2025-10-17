x = list(map(int, input().split()))
a = 1
for i in range(len(x)+1):
    if a < x.count(i):
        a = x.count(i)
print('скок', a)
print([b for b in set(x) if x.count(b) == a])