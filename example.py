# box ={}
# jars={}
# create ={}
# box['biscuit']=1
# box['cake']=3
# jars['jams']=4
# create['box']=box
# create['jars']=jars
# print(len(create[box]))


# dict ={'c':97, 'a':98,'b':98}
# for _ in sorted(dict):
#    print(dict[_])
   
# rec ={"name": "python" ,"age":"20"}
# r=rec.copy()  # it creates different address

# print(id(r)==id (rec))
# print(id(r))
# print(id(rec))

rec ={"name":"python","age":"20"}
id1= id(rec)
del rec
rat ={"name":"python","age":"20"}
id2=id(rat)
print(id1==id2)  # its ans is false but kabhi kabhi true aa     sakta hai


# # this code is about of moving 0s to the endof the list
# val=[0,1,0,3,12]
# for i in val:
#     if i==0:
#         val.remove(i)
#         val.append(i)
# print(val)        

# #find common element in 3 array
# a=[1,2,3]
# b=[2,3,4]
# c= [3,4,5]
# # for i in a:
# #     if i in b and i in c:
# #         print(i) 
# common =set (a) & set(b) & set(c)
# print (common)


#find maximum number of consecutive 1s
# arr=[1,1,0,1,1,1,0,1,1,1,1]
# count = 0
# max_count =0
# for i in arr:
#     if i==1:
#         count+=1
#         if count>max_count:
#             max_count=count
#     else :
#          count =0
# print(max_count)   

#palindrom list
# a = [1,2,3,2,1]
# if a == a[::-1]:
#     print("its an palimndrome")
# else:
#     print("its not palindrome")



# string= "hello"
# reverse=""
# for i in string:
#     reverse=i+ reverse
#     print(reverse)
    
# s = "racecar"
# reverse=""
# for i in s:
#     reverse=i+ reverse
#     print(reverse) 
    
#     if s == reverse:
#         print("its an palindrome")  
#     else:
#         print("its not palindrome")
    
# s = "hello"
# result =""
# for i in s:
#     if i  not in result:
#         result+=i
# print(result)

# s = input("enter the input value:\n")
# result =""
# for i in s:
#     if i  not in result:
#         result+=i
# print(result)

a=[10,11,7,12,14]
total=0
for i in range (len(a)-1):
    total = total+abs(a[i]-a[i+1])
print(total)    

