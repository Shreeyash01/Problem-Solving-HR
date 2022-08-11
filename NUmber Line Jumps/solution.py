a=list(map(int,input().split()))
x1=a[0]
v1=a[1]
x2=a[2]
v2=a[3]

if x1>x2  :
    if v1<v2:
        if (x1-x2)%(v2-v1)==0 :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

elif x1<x2:
    if v1>v2:
        if (x2-x1)%(v1-v2)==0 :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        
else:
    if v1==v2 :
        print("YES")
    else:
        print("NO")
