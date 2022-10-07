l = int(input())

for i in range(l):
    n, c, m = [int(r) for r in input().split()]
    t=n//c
    a=t
    
    if a < m:
        print(t)
        
    else:
        while (a >= m):
            temp = a // m
            t += temp
            a=a-(temp*m)+temp
        print(t)
