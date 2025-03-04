#https://codeforces.com/problemset/problem/1692/A
t = int(input())
while t > 0:
    cont = 0
    l = list(map(int, input().split()))
    for k in range(len(l)):
        if(l[0] < l[k]):
            cont += 1
    print(cont)
    t -= 1