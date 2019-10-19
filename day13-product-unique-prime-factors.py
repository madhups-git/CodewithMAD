# Script to product unique prime factors

n=int(input('Enter a number: '))
p_n=1
for i in range(2,n):
 if(n%i==0):
  p_n*=i
else:
 print ('Product of Prime Factors is %d' %p_n)
