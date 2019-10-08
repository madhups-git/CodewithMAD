# Python Script to check whether a given number is palindrome or not?

n=str(input('Enter a number to check with palindrome: '))
m=n[::-1]
print ('Reverse of a given number: ', m)
if(m==n):
 print ('Palindrome')
else:
 print ('Not a Palindrome')
