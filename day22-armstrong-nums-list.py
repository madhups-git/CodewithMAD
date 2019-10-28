# Script to check number of armstrong numbers in the list

a=[153,370,22,135]

def check_armstrong(n):
  print ('Checking Armstrong for %d' %n)
  sum=0
  m=n
  while(n>0):
    digit=n%10
    iter=3
    pro=1
    while (iter>0):
      pro*=digit
      iter-=1
    sum+=pro
    n=n//10
  else:
    if (m==sum):
      print ('%d is a Armstrong num' %m)
      return(1)
    else:
      return(0)
    
armstrong_count=0
for i in a:
  armstrong_count+=check_armstrong(i)
else:
  print ('%d are the armstrong numbers in the list' %armstrong_count)

