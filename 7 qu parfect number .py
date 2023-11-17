# Write a program to take a number from the user and then determine if that number is a special type of number called a 'perfect number'.
#  A perfect number is a number where the sum of all its factors (excluding the number itself) is equal to the number itself. Print Yes if the number is a perfect number else print No. 
# Test Case1:Input:6,Output:Yes
# Explanation:The program takes the number 6 as input. It then calculates the factors of 6, which are 1, 2, and 3. The sum of these factors (1 + 2 + 3) is equal to 6, so 6 is a perfect number.


n=int(input('enter the number'))
s=0
i=1
while n>i:
    if n%i==0:
        s=s+i
        print(s)
    i=i+1
if s==n:
    print('yes')
else:
    print('no')

