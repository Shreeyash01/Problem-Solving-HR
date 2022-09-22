n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    j=i+1
    for j in range(j,len(a)):
        if a[i]==a[j]:
           b.append(j-i)
        else:
            continue
if len(b)==0 :
    print(-1)
else:
    print(min(b)) 
