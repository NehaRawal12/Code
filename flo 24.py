# Take the number N and the name from the user as inputs, and print the name N times.
# Test Case1:Input:2,Badanti Output:Bedanti ,Bedanti

# a=int(input('enter the number'))
# i=0
# while i<a:
#     print('bedanti')
#     i=i+1

# Take a number N from the Take a number N from the user as input, and print even numbers up to N.
# Test Case1:Input:10,Output:2  4 6 8 

n=int(input('enter the number'))
i=1
while i<n:
    if i%2==0:
        print(i)
    i=i+1