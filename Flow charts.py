# Write a program to take three numbers from the user and print the greater number of the three numbers. (Assume all three numbers are distinct)Test Case1:Input:20,3,43.Output:=43

# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# if a>b and a>c:
#     print(a)
# if b>a and b>c:
#     print(b)
# if c>b and c>a:
#     print(c)


# Write a program to take four numbers from the user and print the greater number of the four numbers. (assume all the numbers are distinct).test Case1:Input:98,13,29,58.Output:98
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# d=int(input('enter the number'))
# if a>b and a>c and a>d:
#     print(a)
# elif b>a and b>c and b>d:
#     print(b)
# elif c>a and c>b and c>d:
#     print(c)
# elif d>a and d>b and d>c:
#     print(d)

# Write a program to take 4 numbers from the user and output the second max of these 4 numbers.Test Case1:Input:5,4,6,7.Output:6

a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('enter the number'))
d=int(input('enter the number'))
if a>b and a>c and a<d:
    print(a)
elif a>b and a>d  and a<c:
    print(a)
elif a>c and a>d and a<b:
    print(a)
if b>a and b>c and b<d:
    print(b)
if b>a and b>d and b<c:
    print(b)
if b>d and b>c and b<a:
    print(b)
if c>a and c>b and c<d:
    print(c)
if c>a and c>d and c<b:
    print(c)
if c>b and c>d and c<a:
    print(c)
if d>a and d>b and d<c:
    print(d)
if d>a and d>c and d<b:
    print(d)
if d>b and d>c and d<a:
    print(d)