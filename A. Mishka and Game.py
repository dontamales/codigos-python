#https://codeforces.com/problemset/problem/703/A
t = int(input())
t2 = t
winM=0
winC=0
draw=0
while t > 0:
    m, c = map(int, input().split())
    if (m > c) :
        winM += 1
    elif (m < c):
        winC += 1
    elif (m == c):
        draw += 1
    t -= 1

if(draw== t2 or winM==winC):
        print("Friendship is magic!^^")
elif(winM>winC) :
    print("Mishka")
else:
    print("Chris")