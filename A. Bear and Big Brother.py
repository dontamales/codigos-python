#https://codeforces.com/problemset/problem/791/A
a, b= map(int, input().split())
cont = 0
while a <= b:
    a = a * 3
    b = b * 2
    cont = cont + 1

print(cont)