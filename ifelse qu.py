# Write a program to take two numbers, A and B from the user. Your task is to find the largest number that is less than A and can be divided evenly by B. Can you figure out that number?
# Test Case1:Input:15,4 Output:12.

# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=a%b
# r=0
# if c==0:
#     print(r)
# else:
#     print((a//b)*b)

# Write a program to take an integer as input and print the smallest positive integer that is a multiple of both 2 and n.
# Test Case:Input:5 Output:10 Test Case:Input:6 Output:6
n=int(input('enter the number'))
a=2
if n%2==0:
    print(n)
else:
    print(n*a)

# n=int(input('enter the number'))
# a=2
# while a%n!=0:
#     a=a+2
# print(a)