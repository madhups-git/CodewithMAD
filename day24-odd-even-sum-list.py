# Script to calculate the sum of even and odd digits of a given number

a=[2,34,456,35]

even_sum=0
odd_sum=0

for i in a:
  while i>0:
    dummy=i%10
    if(dummy%2):
      odd_sum+=dummy
    else:
      even_sum+=dummy
    i=i//10
else:
  print ('The odd sum is %d, The even sum is %d' %(odd_sum,even_sum))
   
