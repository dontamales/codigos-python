#https://codeforces.com/problemset/problem/110/A
n = input()
conte = 0
s = 's'
sa = "mondongo"
for k in range(len(n)):
    if( (n[k] == "4" ) or (n[k] == "7") ):
        conte += 1
        if(s == 'n' and conte > 1):
            sa = "NO"
        else:
            s = 's'
    else:
        s = 'n'


if((conte > 1) and (sa == "mondongo") ):
    print("YES")
else:
    print("NO")
