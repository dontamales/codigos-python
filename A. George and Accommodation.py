#https://codeforces.com/problemset/problem/467/A
n = int(input())
cont = 0
while n > 0:
    a, b = map(int, input().split())
    if (((a + 2) <= b)):
        cont += 1

    n -= 1

print(cont)