# Take a number N from the user as input and repeatedly find the sum of the digits of the number till you get a single digit. Print that digit. Example: 678 -> 6+7+8 = 21 -> 2+1 = 3
# Test Case 1Input:483
# Output:6
# Test Case 2:Input:837,9

n=int(input('enter the number'))
i=1
s=0
while n>0:
    r=n%10
    s=s+r     
    n=n//10
    a=s
    c=0
    while a>0:
        b=a%10
        c=c+b
        a=a//10
print(c)