#https://codeforces.com/problemset/problem/148/A
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
cont = 0
for i in range(1, d +1  , 1):
    if(i % k == 0):
        cont += 1
    elif (i % l == 0):
        cont += 1
    elif (i % m == 0):
        cont += 1
    elif (i % n == 0):
        cont += 1

print(cont)