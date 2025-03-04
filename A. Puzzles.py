#https://codeforces.com/problemset/problem/337/A
n, m = (map(int,input().split()))
f = list(map(int, input().split()))
f.sort()
cont = (f[m-1]) - (f[0])
for k in range(n, m +1, 1):
    ans = f[k - 1] - f[k - n]
    ans = abs(ans)
    cont = min(cont, ans)

print(cont)