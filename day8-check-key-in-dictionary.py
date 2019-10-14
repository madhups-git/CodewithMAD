# Script to check a key is existed in the dictionary or not

d={'1':'Madhu', '2':'Madblocks', '3':'Founder'}

k=(input('Enter a Key to be checked: '))
try:
 print ('Key Found and the element is %s' % d[k])
except:
 print ('Key Not Found')
