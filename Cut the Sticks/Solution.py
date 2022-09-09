n=int(input())
a=list(map(int,input().split()))

while(len(a)>0) :
    print(len(a))
    m=min(a)
    for i in range(len(a)):
        a[i]=a[i]-m
    a = list(filter((0).__ne__, a))
