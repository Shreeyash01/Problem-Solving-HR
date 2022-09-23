def kaprekar(a):
    d = len(str(a))
    n = str(a*a)
    
    l = n[:len(n)-d]
    r = int(n[len(n)-d:])
    
    if l == '':
        l = 0
    l = int(l)
    
    return l+r == a
    
p = int(input())
q = int(input())
c = []
for i in range(p, q+1):
    if kaprekar(i):
        c.append(i)
if len(c) == 0:
    print("INVALID RANGE")
else:
    print(' '.join(str(e) for e in c))
