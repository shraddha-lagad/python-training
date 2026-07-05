# try:
#  a =int(input("enter the valur of A:"))
#  b =int(input("enter the valur of B:"))

#  print(a/b)
# except ZeroDivisionError :
#     print("cannot divide by zero")
# except ValueError:
#     print("special chrarcters are not allowed")
#     print("continue")
    
# try:
#  a =int(input("enter the valur of A:"))
#  b =int(input("enter the valur of B:"))

#  print(a/b)
# except ZeroDivisionError as message:
#     print("cannot divide by zero")
# except ValueError as message:
#     print("special chrarcters are not allowed",message)
#     print("continue")
    
# #multiple exception in singlee except block
# # try:
# #     a=int(input("Enter the value of A"))
# #     b =int(input("enter the valur of B:"))
# #     print(a/b)
# # except(ValueError,ZeroDivisionError) as message:
# #     print(message)
 
#  #default except block   if we have requirement of multiple except block then in that ssituation default except block should be in last other wise syntax error will ecounter
# try:
#     a=int(input("Enter the value of A"))
#     b =int(input("enter the valur of B:"))
#     print(a/b)

# except(ValueError,ZeroDivisionError) as message:
#     print("enter correct number:",message)
# except:
#     print("this id default except block")
    
    #we can use else block if no error wll generate it is depend onn our necessity
# try:
#     a=int(input("Enter the value of A"))
#     b =int(input("enter the valur of B:"))
#     print(a/b)

# except(ValueError,ZeroDivisionError) as message:
#     print("enter correct number:",message)
# else:
#     print("everthing is ok")
 
 
#   # finally block
# try:
#     a=int(input("Enter the value of A"))
#     b =int(input("enter the value of B:"))
#     print(a/b)

# except(ValueError,ZeroDivisionError) as message:
#     print("enter correct number:",message)
# finally:
#     print(" i will always executed")
    
#NESTED TRY  EXCEPT BLOCK

# try:
#     a=int(input("Enter the value of A"))
#     b =int(input("enter the value of B:"))
#     try:
#      print(a/b)
#     except ZeroDivisionError as message:
#      print(message)
# except ValueError as message:
#     print("enter correct number:",message)
# finally:
#     print(" i will always executed")

# #using else and finally

# try:
#     a=int(input("Enter the value of A"))
#     b =int(input("enter the value of B:"))
#     print(a/b)

# except(ValueError,ZeroDivisionError) as message:
#     print("enter correct number:",message)
# else:
#     print("there are no eror in try block")
# finally:
#     print(" i will always executed")


#USER DEFINED EXCEPPTION BY RAISE KEYWORD
# bank_bal =int(input("Eneter amount"))
# if bank_bal<2000:
#     raise Exception("your account balance is below accessing limit")
# else:
#     print("your account has withdrawl")
    
    
# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("this indicates the debugging information")  
# logging.info("this indicates the important information")  
# logging.error("this indicates the error information")  
# logging.warning("this indicates the warnning information")  
# logging.critical("this indicates the critical information")  


import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
try:
    a=int(input("Enter the value of A"))
    b =int(input("enter the valur of B:"))
    print(a/b)

except(ValueError,ZeroDivisionError) as message:
    print("enter correct number:",message)
    logging.exception(message)
    print("logging level id set up check 'newfile.txt' for log details")
else:
    print("everthing is ok")
    
    
    
    