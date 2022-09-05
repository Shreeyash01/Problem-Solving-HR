n=int(input())
for i in range(n):
    s=input()
    cnt=0
    for i in range(len(s)):
        if int(s[i])==0 :
            pass
        else:
            if (int(s) % int(s[i]) == 0) :
                cnt=cnt+1
            else:
                continue
    print(cnt)        
