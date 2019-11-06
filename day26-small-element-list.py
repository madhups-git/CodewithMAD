# Script to find out the smallest element in a list
a=[2,34,1,23]
min=a[0]
for i in a:
  if(i<min):
    min=i
else:
  print ('The small element in the list is %d ' %min)
