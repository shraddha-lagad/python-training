# import re # re module fo performing all regular expression based
# count=0 # to count the number of matching found
# pattern =re.compile("function") # string converts into bytecode
# # print(pattern)'
# matcher=pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters")

#==========================================================================


# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences:",count)

#==========================================================================

# import re
# count=0
# matcher=re.finditer("hi","hihihihi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
#     print("the number of occurrence: ",count)

#==========================================================================

#runtie input
# import re
# obj=input("Enter any character")
# objmatch=re.finditer(obj,"a7b#k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())
 
 
#==========================================================================   

# import re
# a=input("Enter string to perform match operataion")
# match=re.match(a,"Python is very important language")
# print(match)
# if match!=None:
#     print("Match is found at the beginning")
#     print(match.start(),"..",match.end())
# else:
#     print("Match is not found")
 
 #=========================================================================
    
# import re
# a=input("Enter string to perform match operataion")
# match=re.fullmatch(a,"Python is very important language")  #this function match full string 
# print(match)
# if match!=None:
#     print("Match is found ")
#     print(match.start(),"..",match.end())
# else:
#     print("Match is not found")

#==========================================================================

# import re
# a=input("Enter string to perform match operataion")
# match=re.search(a,"Python is very important language")  
# print(match)
# if match!=None:
#     print("Match is found ")
#     print(match.start(),"..",match.end(),"...",match.group())
# else:
#     print("Match is not found")


#==========================================================================
#character classe
# import re 
# match=re.findall('[a-z]',"abch$DhgkftfmLOh&s46@")
# match=re.findall('[A-Z]',"abch$DhgkftfmLOh&s46@")
# match=re.findall('[a-zA-Z]',"abch$DhgkftfmLOh&s46@") 
# match=re.findall('[a-zA-Z0-9]',"abch$DhgkftfmLOh&s46@")
# match=re.findall('[^a-zA-Z0-9]',"abch$DhgkftfmLOh&s46@")
# print(match)  

# import re  # x is replacement
# obj=re.sub('[a-z]','x',"ABCH absd 6754")  
# obj=re.sub('[a-zA-Z]','x',"ABCH absd 6754") #xxxx xxxx 6754
# print(obj)

# import re
# obj=re.subn('[0-7]','#','abc3gd5SH6')
# print(obj)  #abc#gd#SH#
# print("the string is=",obj[0])
# print("the number of replacement is =",obj[1])  #3

# #gmail id or not
# import re
# s=input("Enter mail id")
# obj=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com or *@gmail[.]org",s)
# if obj!=None:
#     print("valid Email")
# else:
#     print("Invalid Email")
    
# import re
# no=input("Enter mobile numbner")
# obj=re.fullmatch("[0-5]\d{9}",no)
# if obj!=None:
#     print("valid num")
# else:
#     print("Invalid number")


import re
a=input("Enter string to perform match operation") # the string we want to search
f=open('myfile2.txt','r')
c=f.read()  #file data
match=re.search(a,c)
print(match)
if match!=None:
  print("Match found at beginning")
  print(match.start(),"",match.end())
else:
    print("there is no matching at beginning level")
