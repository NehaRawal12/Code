a=int(input('enter the number'))
b=int(input('enter the number'))
if a>b:
    max=a
    min=b
else:
    max=b
    min=b
    r=max%min
    while r!=0:
        max=min
        min=r
    r=max%min
hcf=min
lcm=(a*b)//hcf
print(hcf,lcm)