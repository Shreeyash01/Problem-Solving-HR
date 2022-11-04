# s=input()
# n=int(input())

# a=[]
# while(len(a)<n):
#     for i in range(len(s)):
#         if (len(a)<n) :
#             a.append(s[i])
# print(a.count('a'))

st=input()
n=int(input())
c=int(st.count('a')*(n//len(st)) + st[:n%len(st)].count('a'))
print(c)


