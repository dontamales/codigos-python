#https://codeforces.com/problemset/problem/1335/A
import math
t = int(input())
while t > 0:
    n = int(input())
    resultado = math.ceil(n / 2)
    if(n<2):
        print(0)
    else:
        if (n%2 == 0):
            print(n-resultado-1)
        else:
            print(n - resultado)
    t -= 1