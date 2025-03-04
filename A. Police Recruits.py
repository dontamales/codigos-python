#https://codeforces.com/problemset/problem/427/A
n = int(input())
l = list(map(int, input().split()))
contc=0
contp=0
contcsr=0
for k in range(len(l)):
    if(l[k]< 0):
        contc += 1
        if(contp > 0):
            contp -= 1
            contc -= 1
        else:
            contcsr += 1
    else:
        contp += l[k]

print(contcsr)

