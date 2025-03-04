#https://omegaup.com/arena/problem/Calendario-General/
import math
a, b, c = map(int, input().split())
d = math.floor((14-b)/12)
y = c - d
m = b + (12 * d) - 2
h = (a + y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) + math.floor((31*m)/12) )%7
arr = ['DOMINGO', 'LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO']
print(arr[h])