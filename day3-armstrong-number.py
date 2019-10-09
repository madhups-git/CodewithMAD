# Script to check whether given number is Armstrong or not

def cube_n(k,l):
 sum_cube=1
 while l>0:
  sum_cube=sum_cube*k
  l=l-1
 return (sum_cube)
  
n=str(input('Enter a Given Number: '))
count=len(n)
n=int(n)
m=n
sum=0

while m!=0:
 i=m%10
 sum=sum+cube_n(i,count)
 m=int(m/10)

print (sum)
if(sum==n):
 print ('Given %d is an Armstrong Number' % n)
else:
 print ('Given %d is not an Armstrong Number' % n)
