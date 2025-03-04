#https://codeforces.com/problemset/problem/61/A
n = input()
p = input()
cont = ""
for k in range(len(n)):
    if(p[k] == n[k]):
        cont += "0"
    else:
        cont += "1"

print(cont)