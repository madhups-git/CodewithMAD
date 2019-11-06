# Script to find out the range in a list
a=[2,34,1,23]
min=a[0]
max=0
for i in a:
  if(i<min):
    min=i
  if(i>max):
    max=i
else:
  range=max-min
  print ('The range in the list is %d ' %range)
