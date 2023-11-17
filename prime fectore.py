# Write a program to print only the prime factors of a given number 'N'. Take N from the user as input.
# Note: Prime factors are the prime numbers that divide a given number without leaving a remainder.
# Test Case:Input:84
# Output:2,3,7
# Explanation:In this test case, the number given is 84. The program calculates and displays the prime factors of 84, which are 2, 3, and 7. These prime numbers can divide 84 without leaving a remainder.


n=int(input('enter the number'))
i=1
c=0
a=[]
while i<=84:
    if n%i==0:
        a.append (i)
    i=i+1
# print(a)
x=a
p=[]
for j in (x):
    c=0
    for k in range (1,j):
        if j%k==0:
            c=c+1
    if c==1:
        p.append(j)
print(p)
