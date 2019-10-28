# Script to check number of prime elements in a given list

n=[2,25,32,11]

def prime(m):
  print ('Checking %d element in the list' %m)
  fact=2
  for i in range (2,m):
    if m%i==0:
      fact+=1
  else:
    if fact==2:
      return (1)
    else:
      return (0)

prime_count=0
for j in n:
  prime_count+=prime(j)
else:
  print ('The number of prime elements are %d in the list ' %prime_count)
