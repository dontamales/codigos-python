#https://codeforces.com/problemset/problem/344/A
i = int(input())
cont = 0
s = 'p'
for k in range(i):
    n = int(input())
    if(k == 0 and n == 1):
        cont += 1
        s = 's'
    elif(k == 0 and n == 10):
        cont += 1
        s = 'm'
    if(n == 1 and s== 'm' ):
        cont += 1
        s = 's'
    elif(n == 10 and s == 's' ):
        cont += 1
        s = 'm'

print(cont)