n=int(input())

for i in range(n) :
    a=int(input())
    ht=0
    for j in range(a+1):
        if j%2==0 :
            ht=ht+1
        else:
            ht=ht*2
        
    print(ht)
