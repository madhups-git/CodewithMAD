# Python Script to copy elements from one array to another array

a=[]
b=[]

size1=int(input('Enter the Size of First Array: '))
for i in range(size1):
 temp=int(input('Enter the Element of First Array: '))
 a.append(temp)

for i in a:
 b.append(i)

print (a)
print (b)
 
