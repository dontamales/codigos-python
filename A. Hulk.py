#https://codeforces.com/problemset/problem/705/A
n = int(input())
cadena = ""
cont = 0
while n > 0:
    cont += 1
    if(n == 1):
        if (cont % 2 == 0):
            cadena += "I love it"
        else:
            cadena += "I hate it"
    else:
        if (cont % 2 == 0):
            cadena += "I love that "
        else:
            cadena += "I hate that "
    n -= 1

print(cadena)