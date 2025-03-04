#https://codeforces.com/problemset/problem/133/A
p = input()
cont = 0
for k in range(len(p)):
    if(p[k] == 'H' or p[k] == 'Q' or p[k] == '9'  ):
        cont = 1

if(cont > 0):
    print("YES")
else:
    print("NO")