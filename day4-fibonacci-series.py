# Script to print fibonacci series 

a=[]
n=int(input('Enter the number of terms that you want to print in fib series: '))
fib1=0
fib2=1
a.append(fib1)
a.append(fib2)
while n>0:
 fib3=fib2+fib1
 fib1=fib2
 fib2=fib3
 n=n-1
 a.append(fib3)
else:
 print (a)
