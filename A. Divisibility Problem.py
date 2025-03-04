#https://codeforces.com/problemset/problem/1328/A
t = int(input())
while t > 0:
    a, b = (map(int, input().split()))
    if(a%b == 0):
        print(0)
    else:
        print(b-(a%b))
    t -= 1
