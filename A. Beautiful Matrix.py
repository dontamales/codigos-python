#https://codeforces.com/problemset/problem/263/A
matriz = []
cont = 0
for _ in range(5):
    fila = list(map(int, input().split()))
    matriz.append(fila)

f = None
c = None

for i, fila in enumerate(matriz):
    if 1 in fila:
        f = i
        c = fila.index(1)
        break

if(f>2):
    if(f == 3):
        cont += 1
    if(f == 4):
        cont += 2
elif(f < 2):
    if (f == 1):
        cont += 1
    if (f == 0):
        cont += 2

if(c>2):
    if(c == 3):
        cont += 1
    if(c == 4):
        cont += 2
elif(c < 2):
    if (c == 1):
        cont += 1
    if (c == 0):
        cont += 2

print(cont)