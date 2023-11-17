a=[]
for i in range(10):
    x=input('enter value')
    a.append(x)
print ('origanal list',a)
index=int(input('enter index where u want to insert'))
value=input('enter value to insert')
a.insert(index,value)
print('list after insertion',a)