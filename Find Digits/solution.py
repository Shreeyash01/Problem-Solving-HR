m=int(input())
for i in range(m):
    a=input()
    cnt=0
    for i in range(len(a)):
        if int(a[i])==0 :
            pass
        else:
            if (int(a) % int(a[i]) == 0) :
                cnt=cnt+1
            else:
                continue
    print(cnt)        
