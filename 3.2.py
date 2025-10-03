def binladden(n):
    k = 2
    fbi = []
    while n > 1:
        while n % k == 0:
            fbi.append(k)
            n = n // k
        k += 1
    print(fbi)
binladden(int(input()))