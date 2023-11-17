# first max
# a=int(input('enter the number'))
# b=int(input('enrer the numbr'))
# c=int(input(''))
# d=int(input('numbr'))
# e=int(input('enter thenumber'))
# f=int(input('enter the number'))
# if a>b:
#     max=a
# else:
#     max=b
# if c>d:
#     max2=c
# else:
#     max2=d
# if e>f:
#     max3=e
# else:
#     max3=f
# # print(max,max2,max3)
# if max>max2:
#     if max>max3:
#         print(max)
# else:
#     if max2>max3:
#         print(max2)
#     else:
#         print(max3)
a=int(input('number'))
b=int(input('number'))
c=int(input('number'))
d=int(input('number'))
e=int(input('number'))
if a>b:
    max=a
else:
    max=b
if c>d:
    max2=c
else:
    max2=d
if max>max2:
    if max>e:
        print(max)
    else:
        print(e)
else:
    if max2>e:
        print(max2)   
    else:
        print(e)