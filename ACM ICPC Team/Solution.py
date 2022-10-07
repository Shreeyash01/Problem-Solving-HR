# a = list(map(int,input().split()))
# b = []
# for i in range(a[0]):
#     c = input()
#     b.append(c)
# d=[]
# for i in range(a[0]):
#     j = i + 1
#     for j in range(j,a[0]):
#         res=" "
#         for l in range(a[1]):
#             res=res+str(int(b[i][l]) or int(b[j][l]))
#         r=res.count('1')
#         d.append(r)
# m=max(d)
# print(m)
# print(d.count(m))

N,k=map(int,input().split())
l=[]

for i in range(N):
    l.append(int(input(),2))
    
mtopics=-1
teams=1

for i in range(N):
    for j in range(i+1,N):
        topics=len([k for k in bin(l[i]|l[j]) if k=='1'])
        if(topics>mtopics):
            teams=1
            mtopics=topics
        elif(topics==mtopics):
            teams+=1
            
print(mtopics)

print(teams)
