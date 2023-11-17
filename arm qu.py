# Write a program to print all Armstrong numbers in a given range of M to N.
# Test Case1:Input:100  ,1000
# Output:153,370,371,407

a=int(input('enter the number'))
b=int(input('enter the number'))
for i in range(a,b):
    sum=0
    org=i
    while i>0:
        # print(org,'org')
        # print(i,'i')
        r=i%10
        sum=sum+r**3
        i=i//10
    # print(s)
    if sum==org:
        print(org,'arm')

        # zzzzzoppzzzzzzppzz
    