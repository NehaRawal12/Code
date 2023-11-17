# Write a program to take two numbers from the user as input and obtain the HCF and LCM of the two numbers.
# Test Case1 Input:12,15:Output:3,60
a=int(input('enter the number'))
b=int(input('enter the number'))
hcf=1
if a>b:
    max=a
else:
    max=b
for i in range (1,max+1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=(a*b)//hcf
print(hcf ,lcm)