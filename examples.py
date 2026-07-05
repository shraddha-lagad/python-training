def f(i,values=[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3)



arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
    for i in range(0,6):
        print(arr[i], end="")
        
        
fruit_list1 =['Apple' ,'berry', 'cherry','papaya']
fruit_list2 =fruit_list1
fruit_list3=fruit_list1[:]
fruit_list2[0]='guava'
fruit_list3[1]='kiwi'

sum =0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0] =='guva':
        sum+= 1
    if ls[1]=='kiwi':
        sum+= 20
print(sum, end=" ")


for i ,j in zip(range(1,6), range(5,0,-1)):
  if i==3 and j==3:
      continue
  print(i," ",j)   