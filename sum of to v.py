# Write a program to take two integers M, and N and print the sum of numbers in the range M to N.
# Test Case1:Input:2,7 Output:27 
# Explanation:Output should be 27 as the sum of numbers (2+3+4+5+6+7=27)

m=int(input('enter the number'))
n=int(input('enter the number'))
s=0
for i in range (m,n+1):
    s=s+i
    print(s)
