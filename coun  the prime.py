# Write a program to take a number and print the count of the prime numbers that are strictly less than a number.
# Testcase 1:Input: 10,Output: 4 Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Testcase 2:Input: 0 Output: 0 test case3: input 2 output=0
      
a=int(input('enter the number'))
z=0
q=2
while q<=a:
    i=1
    c=0
    while i<=q:
        if q%i==0:
            c=c+1
        i=i+1
    if c==2:
        z=z+1 
    q=q+1
print(z)
        




# s=5
# i=0
# while i<5:
#     if i != 0:
#         k=0
#         while k<i:
#             print(" ", end= " ")
#             k+=1
#     j=1 
#     while j<=s:
#         print(j,end=" ")
#         j+=1
#     print()
#     s-=1
#     i+=1
