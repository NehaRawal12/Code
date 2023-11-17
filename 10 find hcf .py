# Write a program to take N numbers from the user and print the Highest Common Factor (HCF) of the given set of numbers. Take N from the user as input.
# Test Case1:Input:4,12,18,24,30.Output:6
# Explanation:In this test case, the user inputs four numbers: 12, 18, 24, and 30. The program then calculates the HCF of these numbers, which is found to be 6. This means that 6 is the largest number that can divide all the given numbers (12, 18, 24, and 30) without leaving a remainder.

# n=int(input('enter the number'))
# hcf=1
# for i in range (n):
#     num=int(input('enter the number'))
#     m=0
#     x=0
#     if num>m:
#         max=num
#     else:
#         max=x
#     for r in range(1,max+1):
#         if m%r==0 and num%r==0:
#             hcf=r
# print(hcf)

n = int(input("Enter the number of values: "))

# Input the first number

hcf = int(input("Enter the first number: "))
print(hcf)

# Input the remaining numbers and find the HCF iteratively
for i in range(n - 1):
    num = int(input("Enter the next number: "))
    print(num)
    
    # Find the HCF of the current HCF and the new number
    while num:
        hcf, num = num, hcf % num
        print(num)
        print(hcf)

# Print the result
print("HCF:", hcf)