# init_tuple=()
# print(init_tuple.__len__())# defaault value 0


# init_tuple_a ='a','b'
# init_tuple_b =('a','b')
# print(init_tuple_a == init_tuple_b) # true

# l=[1,2,3]
# init_tuple =('python',) *(l.__len__() - l[::-1][0])
# print(init_tuple)

# a={(1,2):1,(2,3):2 ,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# # print(a['a','b'])  # key error only one key may use



# fruit={}
# def addone(index):
#     if index in fruit:  # in is membership opera
#         fruit[index] +=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


arr={}
arr[1]=1
arr['1']=2
arr[1] +=1
sum =0
for k in arr:
    sum +=arr[k]
print(sum)


# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4 #here we consider 1.0 and 1 same 
# print(my_dict)
# sum =0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict: 
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# print(int(True)) #1
# print(int(False)) #0
# print(float("4")) #4.0
# print(float(4.22)) #4.22    
# print(bool(-1)) #True
# print(bool(0)) #false


my_dict={}
my_dict[1]=1
my_dict['1']=2
my_dict[1.0]=4 #here we consider 1.0 and 1 same 
print(my_dict)
sum =0
for k in my_dict:
    sum+=my_dict[k]
print(sum)

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict: 
    sum += my_dict[k]
print(sum)
print(my_dict)

print(int(True)) #1
print(int(False)) #0
print(float("4")) #4.0
print(float(4.22)) #4.22    
print(bool(-1)) #True
print(bool(0)) #false