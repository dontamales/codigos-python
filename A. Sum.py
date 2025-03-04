#https://codeforces.com/problemset/problem/1742/A
t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    if (((a+b) == c) | ((a+c) == b) | ((b+c) == a)):
        print("YES")
    else:
        print("NO")
    t -= 1