# Write a program to print the sum of odd numbers up to N.
# Test Case1:Input:20,Output:100

n=int(input('enter the number'))
i=0
s=0
while i<n:
    if i%2!=0:
        s=s+i
    print(s)
    i=i+1
