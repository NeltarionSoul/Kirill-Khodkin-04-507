# a,b - Natural, a,b<150
# Exist x (+): a+x%b == (b+x)%a == 0
# Find x
a = int(input())
b = int(input())
for x in range(150^2):
    if (a+x) % b == (b+x) % a == 0:
        print(x)
        break