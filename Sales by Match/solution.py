n=int(input())
a=list(map(int,input().split()))

cnt=0

for i in range(len(a)):
    if a[i]==0 :
        pass
    else:       
    	j=(i+1)
    	for j in range(j,len(a)):
    	    if a[i]==a[j]:
    	        cnt=cnt+1
    	        a[i]=0
    	        a[j]=0
    	        break
    	    else:
    	        continue

print(cnt)
