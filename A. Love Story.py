#https://codeforces.com/problemset/problem/1829/A
t = int(input())
valores = "codeforces"
while t > 0:
    cont = 0
    valores2 = input()
    for i, k in enumerate(valores):
        if k != valores2[i]:
            cont += 1
    print(cont)
    t -= 1
