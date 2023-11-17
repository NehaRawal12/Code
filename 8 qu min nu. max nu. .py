# Write a program to take N numbers from a user as input, and print the maximum and minimum values among the given set of N numbers. Also, take N from the user as input. 
# # Test Case1:Input:5,10,5,8,3,12.Output:12,3
# N = int(input("Enter the value of N: "))
# maximum = 0
# minimum = 0
# for i in range(N):
#     num = int(input("Enter a number: "))
#     if num > maximum:
#         maximum = num
#     if  num < minimum:
#         minimum = num
# print("Maximum value:", maximum)
# print("Minimum value:", minimum)


# N = int(input("Enter the value of N: "))
# maximum = float
# minimum = float

# for i in range(N):
#     num = int(input("Enter a number: "))
    
#     # For the first iteration, set the initial values
#     if  num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num

# print("Maximum value:", maximum)
# print("Minimum value:", minimum)
b=int(input('enter the number'))
n=int(input('enter the number'))
max=n
min=n
print(max)
print(min)
print(n)
for i in range(b):
    n=int(input('enter the number'))
    print(n)
    if n>max:
        max=n
        print(max,'max')
    if n<min:
        min=n
        print(min,'min')
print(max)
print(min)