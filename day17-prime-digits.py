# Script to check number of prime digits in a given n digit number

n=int(input('Enter a number: '))
prime_count=0
while n>0:
 fact=2
 dummy=n%10
 for i in range(2,dummy):
  if(dummy%i==0):
   fact+=1
 n=n//10
 if(fact==2 and dummy!=0):
  prime_count+=1
print ('The number of prime digits are %d' % prime_count)
