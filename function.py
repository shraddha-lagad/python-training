# #positional argument
# def msg(val1,val2):
#     print("value 1 ",val1)
#     print("value 2 ",val2)

# #calling function    this will call first
# msg("admin","help4code")

# #keyword argument
# def msg2(val1,val2):
#     print("value 1 ",val1)
#     print("value 2 ",val2)

# #calling function    this will call first
# msg2(val1="admin",val2="help4code")

# #default argument
# def city(cityname="Nagpur"):  # when value will not pass thrn nagpur will execute
#     print("cityname=",cityname)
# city("mumbai")
# city("pune")
# city()  #Nagpur

# #variable length argumrnt/variable number of argument
# def cityName(*city):  # this will except all value
#     print(city)
# cityName("Nagpur","Mumbai","Pune","Nashik")

# def arithimatic(a,b):
#     add=a+b
#     sub=a-b
#     mult=a*b
#     div=a/b
#     return add,sub,mult,div   # return multiple value at the same time
# print(arithimatic(5,5))  # it gives tuple because value do not change on runtime tuple is immutable
    
# Nested loop
for i in range(1,4): #outer loop - rows  i will remain constat 
    for j in range(1,4): # inner loop column  it changes
        print(i,end=" ")
    print() # goes to next line/row


# input rows
# n=int(input("Enter the number of rows"))
# for i in range(1,n+1): #--
#     for j in range(1,n+1): #|
#         print(i,end=" ")
#     print() 
 
 
 # reverse    
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()
 
 # star pattern   
# n=int(input("Enter rows :"))
# for i in range(1,n+1):
#     print("*"*i)
    
# n=int(input("Enter rows :"))
# for i in range(1,n+1):
#     # for j in  range(1,1+i):
#         print(chr(64+i),end=" ")  # chr function convert integer value into ascii code
#     # print()
  
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print("*", end=" ")
#     print()  

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#        print(chr(64+j),end=" ")
#     print()

import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#      for j in range(1,n+2-i):
#         time.sleep(1)
#         print(n+1-i,end=" ")
#      print()

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#      for j in range(1,n+2-i):  
#         print(chr(65+n-i),end=" ")
#      print()

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):  
        time.sleep(1)
        print("*",end=" ")       
    print()

