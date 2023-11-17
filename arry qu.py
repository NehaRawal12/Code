# Write a program to take N numbers from a user as input and store them in an list then take another number from the user M, and delete the Mth element from the list print the final list. 
# Note - (Do not use another )
# Test Case 1:Input:5,2 4 2 6 3
# 3
# Output:
# 2 4 6 3
# Test Case 2:
# Input:6,,2 4 6 3 3 9
# 2
# Output:2 6 3 3 9

# a=[]
# s=int(input('enter the numnbe'))
# for i in range (s):
#     v=int(input('enter the number'))
#     a.append(v)
# print(a)
# m=int(input('enter the number to delet'))
# f=0
# for i in range (s):
#     if a[i]==m:
#         f=1
#         p=i
#         break
# if f==0:
#     print('no')
# else:
#     for i in range(p,s-1):
#         a[i]=a[i+1]
#     a.pop()
#     print(a)

# i=2
# s=0
# c=0
# while i<=10:
#     if i%2==0:
#         s=s+i
#         c=c+1
#     i=i+1
# print(s,c)



# i=2
# s=0
# c=0
# while s<=10:
#     if i%2==0:
#         s=s+i
#         c=c+1
#     i=i+1                                                                                      
# print(c,s)


# i=3
# s=0
# while i<=9*3:
#     s=s+i*i
#     i=i+3
#     print(i)
# print(s)

# sum of n

n=int(input('enter the number'))
i=1
s=0
while i<=n:
    s=s+1/i
    i=i+1
print(s)
