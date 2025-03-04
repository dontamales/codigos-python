#https://codeforces.com/problemset/problem/758/A
n = int(input())
a = list(map(int, input().split()))
a.sort()
cont = 0
for k in range(len(a) - 1, -1, -1):
    cont += ((a[len(a) - 1]) - a[k] )

print(cont)