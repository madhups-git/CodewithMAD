# Script to print sum of squares of n natural numbers

n=int(input('Enter a number to calculate the squares of natural numbers: '))
m=n
sum=0
while n>0:
 sum+=(n*n)
 n=n-1
else:
 print ('Sum of Squares of %d Natural Numbers is %d' % (m,sum))
