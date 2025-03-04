#https://codeforces.com/problemset/problem/266/A
n = int(input())
p = input()
cont = 0
for k in range(len(p) - 1):
    if (p[k + 1] == p[k]):
        cont += 1
print(cont)
