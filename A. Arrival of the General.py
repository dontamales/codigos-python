#https://codeforces.com/problemset/problem/144/A
n = int(input())
i = list(map(int, input().split()))
cont = 0
vmm = i[0]
posmm = 0
posm=0
todos_iguales = all(x == i[0] for x in i)
if todos_iguales:
    print(0)
else:
    for k in range(len(i) - 1):
        if i[k + 1] <= vmm:
            posmm = k + 1
            vmm = i[k + 1]
    i.append(i.pop(posmm))
    cont = (len(i) - 1) - (posmm)
    vm = i[0]
    for j in range(len(i) - 1):
        if i[j + 1] > vm:
            posm = j + 1
            vm = i[j + 1]

    cont += posm
    print(cont)