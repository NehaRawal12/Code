# Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example, 153 = 1^3 + 5^3 + 3^3.)
# Test Case1:Input:370 Output:Yes 
# Test Case2:Input:121 Output:No

x=int(input('enter the number'))
a=x
y=x
s=0
c=0
while a>0:
    r=a%10
    c=c+1
    a=a//10
while y>0:
    r=y%10
    s=s+r**c
    y=y//10
if s==x:
    print(x,'arm')
else:
    print(x,'no')