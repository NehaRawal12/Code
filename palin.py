# Write a program to check whether a number is palindrome or not.
# Note: A palindrome is a sequence of characters (or numbers) that reads the same 
# forwards as it does backwards. In other words, it remains unchanged when reversed.
# Test Case1:Input:242 Output:Yes,Test Case2:Input:1351O,utput:No


# n=int(input('enter the number'))
# o=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if o==rev:
#     print('yes')
# else:
#     print('no')

a=int(input('enter the number'))
i=1
c=0
while i<=a:
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print(a,'yes')
else:
    print(a,'no')