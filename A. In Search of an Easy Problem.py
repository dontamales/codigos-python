#https://codeforces.com/problemset/problem/1030/A
n = int(input())
i = list(map(int, input().split()))
if(sum(i) > 0):
    print("HARD")
else:
    print("EASY")