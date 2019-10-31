# Script to calculate the maximum element in a given list

a=[2,3,45,54,33]

max=0
for i in a:
  if i>max:
    max=i
else:
  print ('The maximum element is %d' % max)
