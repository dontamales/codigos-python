#https://codeforces.com/problemset/problem/706/B
n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())

def busqueda_binaria(valor):
    ini = 0
    fin = len(x) - 1

    if valor < x[ini]:
        return -1
    if valor >= x[fin]:
        return fin

    while ini <= fin:
        puntero = (ini + fin) // 2
        if ((valor >= x[puntero]) & (valor < x[puntero + 1])):
            return puntero
        elif valor > x[puntero]:
            ini = puntero + 1
        else:
            fin = puntero - 1

    return -1



while q > 0:
    m = int(input())
    print(busqueda_binaria(m) + 1)

    q -= 1