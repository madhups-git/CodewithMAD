# Python Script to reverse a given string
# Python3 Only 
# If you want to run the following scripts in Python 2 use raw_input instead of input

n=str(input('Enter a String to be reversed: '))
n=n[::-1]
print (n)

n=str(input('Enter a String to be reversed: '))
m=''
for i in n:
 m=i+m
print (m)

n=str(input('Enter a String to be reversed: '))
n=n.split(' ')
m=''
for i in (n):
 m+=n[-1] + ' '
 n=n[:-1]

print (m)
