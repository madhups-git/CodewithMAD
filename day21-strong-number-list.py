# Script to check num of strong numbers in the list

a=[2,5,24,120]

def factorial_n(n):
 sum=1
 m=n
 while n>0:
  sum*=n
  n-=1
 else:
  if(sum==m):
    print ('%d is a Strong Number' %m)
    return(1)
  else:
    return (0)
  
strong_count=0
for i in a:
  strong_count+=factorial_n(i)
else:
  print('The number of strong elements are %d in the list' %strong_count)
