# Script to calculate the number of even and odd digits of a given n digit number

n=int(input('Enter a given number: '))
even_count=0
odd_count=0

while n>0:
 if(n%10%2):
  odd_count+=1
 else:
  even_count+=1
 n=n//10
print ('The number of even digits are %d and odd digits are %d' %(even_count,odd_count))
