n=int(input())

for i in range (n):
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    
    b=x[0]
    w=x[1]
    bc=y[0]
    wc=y[1]
    z=y[2]
    
    if bc+z<wc :
        print((b*bc)+(w*(bc+z)))
    elif wc+z<bc :
        print((b*(wc+z))+(w*wc))
    else:
        print((b*bc)+(w*wc))
    
    
