# Script to find out the next palindrome number after a given number
a=int(input('Enter a number: '))

def palindrome(n):
  m=str(n)
  m=m[::-1]
  if(str(n)==m):
    return (1)
  else:
    return (0)

b=a+1
while True:
  k=palindrome(b)
  if(k==1):
    print ('The palindrome element after %d is %d' %(a,b))
    break
  b=b+1
