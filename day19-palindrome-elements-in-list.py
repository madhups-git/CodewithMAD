# Number of palindrome elements in the list

a=[23,32,11,141,22]

def palindrome_check(m):
 l=str(m)[::-1]
 if(m==int(l)):
  return (1)
 else:
  return (0)
 
palindrome_count=0
for i in a:
  palindrome_count+=palindrome_check(i)
 
print ('The number of palindrome elements are %d' % palindrome_count)
