a=list(map(int,input().split()))
b=list(map(int,input().split()))

d1=a[0]
m1=a[1]
y1=a[2]
d2=b[0]
m2=b[1]
y2=b[2]

if y1==y2 :
    if m1==m2 :
        if d1==d2 :
            print('0')
        elif(d1<d2) :
            print('0')
        else:
            print((d1-d2)*15)
    elif(m1<m2):
        print('0')
    else:
        print((m1-m2)*500)
elif(y1<y2):
    print('0')
else:
    print((y1-y2)*10000)
                            
            
    
