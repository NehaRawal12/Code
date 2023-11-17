# Write a program to input a number and check whether it is a perfect square or not.
# Note: A perfect square is the product of some integer with itself. 
# Test Case1:Input:16 output Yes
# Test Case2Input:14 Output:No

a=int(input('eter the number'))
i=0
s=0
while a>=i*i:
    s=i*i
    # print(s)
    if s==a:
        # print('yes')
        break
    i=i+1
if s==a:
    print('yes')
else:
    print('no')
