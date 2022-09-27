p,d,m,s = map(int,input().split())
cnt = 0

while s>0:
    s -= p
    p -= d
    if p<=m:
        p = m
    if s<0:
        break
    cnt += 1
    
print(cnt)

    
# p, d, m, s = [int(r) for r in input().split()]
# t = p
# cnt = 0

# if t >= s:
#     print(cnt)
# else:
#     while (p > m):
#         p = p - d
#         t = t + p
#         cnt += 1
#         if t >= s:
#             break
#         else:
#             continue

#     while (t < s):
#         t = t + m
#         cnt = cnt + 1

#     print(cnt)
