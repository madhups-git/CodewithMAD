# Script to find out the next Armstrong number after a given number

a=int(input('Enter a number: '))

def sum_power(k,p):
  mul=1
  while p>0:
    mul*=k
    p-=1
  return (mul)



def armstrong(n):
  b=0
  dummy=n
  l=len(str(n))
  n=int(n)
  #print (n,l)
  while n>0:
    m=n%10
    b+=sum_power(m,l)
    n=n//10
    print 
  else:
    if(dummy==b):
      return (1)
    else:
      return (0)

c=a+1
while True:
  d=armstrong(c)
  if(d==1):
    print ('The Armstrong number after %d is %d' %(a,c))
    break
  c=c+1



  
