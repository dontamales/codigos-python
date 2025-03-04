#https://codeforces.com/problemset/problem/1807/A
t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    if((a+b)==c):
        print ("+")
    else:
        print("-")

    t -= 1
