a=int(input('enter the number'))
orig=a
rev=0
while (a>0):
    rev=(rev*10)+a%10
    a=a//10
if rev==orig:
    print('palindrome number',orig)
else:
    print('no',orig)

# n=int(input('enter the number'))
# s=0
# r=0
# while n>0:
#     r=n%10
#     n=n//10
#     s=s+r
# print(s)