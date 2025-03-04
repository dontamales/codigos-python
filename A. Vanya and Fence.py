#https://codeforces.com/problemset/problem/677/A
a, b = map(int, input().split())
i = list(map(int, input().split()))
cont = 0
for k in i:
    if(k > b):
        cont = cont + 2
    else:
        cont = cont + 1
print(cont)
