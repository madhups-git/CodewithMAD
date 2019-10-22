# Script to check strong number or not

def factorial_n(n):
 sum=1
 while n>0:
  sum*=n
  n-=1
 else:
  return(sum)
  
m=int(input('Enter a number: '))
k=m
strong_sum=0
while k>0:
  strong_sum+=factorial_n(k%10)
  k=k//10
else:
  if(m==strong_sum):
    print ('%d is a Strong Number' % m)
  else:
    print ('%d is not a Strong Number' % m)
 
