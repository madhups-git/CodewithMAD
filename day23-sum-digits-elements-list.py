# Script to calculate the sum of all digits of all elements in a given list

a=[2,34,456,1234]

def sum_list_element(k):
  sum_element=0
  while k>0:
    sum_element+=k%10
    k=k//10
  else:
    return(sum_element)

sum_list=0
for i in a:
  sum_list+=sum_list_element(i)
else:
  print("The sum is %d" %sum_list)
