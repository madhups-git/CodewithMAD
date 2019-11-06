# Script to find out the next prime number after a given number

a=int(input('Enter a number: '))

def prime(n):
  fact=2
  for i in range(2,n):
    if n%i==0:
      fact+=1
  else:
    if(fact==2):
      return(1)
    else:
      return(0)


c=a+1
while True:
  d=prime(c)
  if(d==1):
    print ('The prime number after %d is %d' %(a,c))
    break
  c=c+1



  
