# Script to create a list of numbers in range and sum of the digits less than 10
# And also the numbers should be a perfect square

def perfect_square(p):
 for i in range(p+1):
  if (i*i==p):
   return (1)
 else:
  return (0)

def sum_of_digits(s):
 sum=0
 while s>0:
  sum+=s%10
  s=int(s/10)
 if(sum<10):
  return(1)
 else:
  return(0)

low_value=int(input('Enter the lower value: '))
high_value=int(input('Enter the higher value: '))
k=[]
for j in range(low_value,high_value+1):
 if(perfect_square(j) and sum_of_digits(j)):
  k.append(j)

print (k)
