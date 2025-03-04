#https://codeforces.com/problemset/problem/116/A
t = int(input())
sum = 0
sumt = 0
while t > 0:
    a, b = map(int, input().split())
    sum = sum  + (b-a)
    if (sum > sumt):
        sumt = sum

    t -= 1
print(sumt)