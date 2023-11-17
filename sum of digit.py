# Write a program to take a number from the user and print the sum of the digits of the given number.
# Test Case1:Input:456,Output:15 .Explanation:4+5+6 = 15
# a=int(input('enter the number'))
# s=0
# while(a>0):
#     s=s+(a%10)
#     a=a//10
# print(s)


# Write a program to take a number from the user and print the number digits in the given number.
# Test Case1:Input:456 Output:3

# a=int(input('enter the number'))
# c=0
# while a>0:
#     a%10
#     c=c+1
#     a=a//10
# print(c)

# Write a program that takes a number from the user and prints the number that is formed by reversing the digits of the number.
# Test Case1:Input:123 Output:321

n=int(input('enter the number'))
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
print(rev)
