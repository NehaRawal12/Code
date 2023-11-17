# Write a program to take a number from the user and print all the factors of the given number. A factor is a number that can divide another number evenly without leaving a remainder.
# Test Case1:Input:12 Output:1 ,2,3,4,6,12
# Test Case2:Input:25 Output:1 ,5,25

a=int(input('enter the number'))
i=1
while a>=i:
    if a%i==0: 
        print(i)
    i=i+1

