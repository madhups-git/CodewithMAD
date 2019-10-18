#Python Script to swap two numbers
a=int(input('Enter first number to be Swapped: '))
b=int(input('Enter second number to be Swapped: '))

print ('%d is a, %d is b' % (a,b))

a=a+b
b=a-b
a=a-b

print ('%d is a, %d is b' % (a,b))
