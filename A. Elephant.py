#https://codeforces.com/problemset/problem/617/A
import math
x = int(input())
if (x%5 != 0):
    print(math.floor(x / 5) + 1)
else:
    print(math.floor(x / 5))
