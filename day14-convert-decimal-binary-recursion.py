t=''
def recursive_bin(m):
  global t
  if m>0:
    t+=str(m%2)
    m=m//2
    recursive_bin(m)
  else:
    print (t[::-1])
  
n=int(input('Enter a number to be converted: '))
recursive_bin(n)
