# # class Student: 
# #     rollno=101 #data member
    
# #     def msg(self):  #member function
# #         print("hello world")
# # obj =Student()
# # print(obj.rollno)
# # obj.msg()

# # class Demo:
# #     def __init__(self) :
# #         print("hiii i am a constructor and i always called first")
# #     def info(self):
# #         print("one object")

# # obj= Demo()
# # obj.info()
# # obj2=Demo()   

# # class hod:
# #     def __init__(self) :  #constructor
# #         self.name="prshant jha"
# #         self.age=23
# #         self.empid=101
# #     def info(self):   # instance method
# #         print("my name is:",self.name ) 
# #         print("my age is:",self.age ) 
# #         print("my empid is:",self.empid )    
# # obj=hod()   #object cretaed
# # obj.info()
# class hod:
#     def __init__(self,name,age,rollno) :
#       self.name=name
#       self.age=age
#       self.rollno=rollno
    
#     def show(self):
#         print('name=',self.name) 
#         print('age=',self.age) 
#         print('rollno=',self.rollno) 
# obj =hod('arjun',23,303)
# obj.show()

# class new():    # instance variable
#     def __init__(self) :
#      self.a=10
# obj1=new()
# obj2=new()
# obj3=new()
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# class New:
#     a=10 #static var
#     def __init__(self) -> None:
#        self.name="prashant"
# obj1=New()
# obj2=New()
# obj3=New()   
# New.a=40
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
       
class College:
    collegename="MOdern college" # static var(1 memory)
    def __init__(self):
        self.studentname ="shraddha lagad"   #instance var (3 separe memory)
principal =College()
Teacher=College()
accountant=College()
print("principal =" ,principal.collegename, "..." , principal.studentname) 
print("Teacher =" ,Teacher.collegename, "..." , Teacher.studentname) 
print("accountant =" ,accountant.collegename, "..." , accountant.studentname) 

College.collegename="hbd"
principal.studentname="prashant jha"  
print("principal=",principal.collegename,"|",principal.studentname)  
print("Teacher=",Teacher.collegename,"|",Teacher.studentname)           
print("accountant=",accountant.collegename,"|",accountant.studentname) 


#accessing and deleting varianle from cthe class
# class Student:
#     def __init__(self):
#           self.s_name=input("enter your name")
#           self.s_roll=101
#     def getdata(self):
#         self.s_mb= 69486772934 
# obj =Student()
# obj.getdata()
# obj.s_branch = "CS"
# del obj.s_roll
# print(obj.__dict__)
  
  
#   #static method           
# class Student:
#     @staticmethod
#     def get_personal_details(firstname,lasstname):
#         print("your personal detail=",firstname,lasstname)
#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#          print("your contact detail=",mobile_no,rollno)
# Student.get_personal_details("prashat","jha")
# Student.contact_detail(36835329952,1001)
                 