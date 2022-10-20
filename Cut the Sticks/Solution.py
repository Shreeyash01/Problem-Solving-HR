p=int(input())
b=list(map(int,input().split()))

while(len(b)>0) :
    print(len(b))
    m=min(b)
    for i in range(len(b)):
        b[i]=b[i]-m
    b = list(filter((0).__ne__, b))
