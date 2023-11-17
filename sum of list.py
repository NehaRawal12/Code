l=[1,2,3,4,5,6,7,8,9]
s=0
i=0
while i<len(l):
    a=i+1
    j=1
    c=0
    print('cheking for',a)
    while j<=a:
        if a%j==0:
            c+=1
            
        j=j+1
    if c==2:
        print( l[i])
        s=s+l[i]
    i=i+1
print(s)