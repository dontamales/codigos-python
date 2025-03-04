#https://codeforces.com/problemset/problem/282/A
n = int(input())
cont = 0
while n > 0 :
    a = input()
    if(a[0] == '+' or a[1] == '+' or a[2] == '+'):
        cont += 1
    else:
        cont -= 1
    n -= 1
print(cont)
