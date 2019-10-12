# Script to check whether given number is pronic or not

def check_pronic(m):
 for i in range (1,m):
  if(m==i*(i+1)):
   return (1)
 else:
  return (0)
  
n=int(input('Enter a Number to be checked: '))
if(check_pronic(n)):
 print ('Given %d number is Pronic' % n)
else:
 print ('Given %d number is not Pronic' % n)
