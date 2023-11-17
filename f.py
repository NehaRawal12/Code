# Write a program to take 5 numbers from the user and print the frequency of every number.
# Test Case1:Input:3,4,6,3,6


# a=[2,2,3,4,5,5]
# i=0
# j=0
# c=0
# x=[]
# while i<len(a):
#     while j<len(a):
#         if a[i]==a[j]:
#            c=c+1
#         j=j+1
#     if a[j] not in x:
#         x.append (a[i])
#         print(a[i],c)
#     i=i+1
        
a=[3,4,6,3,6]
i=0
b=[]
while i<len(a):
    c=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1 
        j=j+1 
    if a[i] not in b:
        b.append(a[i]) 
        print(a[i],c)
    i=i+1
    

