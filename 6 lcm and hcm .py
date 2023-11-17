# Write a program to take two numbers from the user as input and obtain the HCF and LCM of the two numbers.Test Case1:
# Input:12,15.Output:3,60

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a>b:
    max=a
else:
    max=b
hcf = 1
for i in range(1, max + 1):
    if a%i == 0 and b%i == 0:
        hcf = i
lcm = (a*b) // hcf
print("HCF of",a, "and",b, "is", hcf)
print("LCM of",a, "and",b, "is", lcm)
