# Script to find out the reverse of all elements in a given list

a=[23,34,56,789]
b=[]

for i in a:
  b.append(int(str(i)[::-1]))
else:
  print (b)
