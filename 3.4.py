def shaman(a,b):
    if a%2 == 0:
        for i in range(a//2+1):
            k = (b)*i
            print(k)
        for i in range(a//2, 0, -1):
            k = (b)*i
            print(k)
    else:
        for i in range(a//2+1):
            k = (b)*i
            print(k)
        for i in range(a//2+1, 0, -1):
            k = (b)*i
            print(k)
shaman(int(input()), str(input()))