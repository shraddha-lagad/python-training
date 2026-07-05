#single level inheritsnce
# class College: #parent classs
#     def college_name(self):  #member func of college
#         print("modern college")
# class Student(College): #child class
#     def student_info(self):
#         print("Name:shradha")
#         print("branch:it")
# obj =Student() #object created for child class
# obj.college_name()
# obj.student_info()
 
 
#  #multilevel inheritance
# # class College: #parent classs
# #     def college_name(self):  #member func of college
# #         print("modern college")
# # class Student(College): #child class
# #     def student_info(self):
# #         print("Name:shradha")
# #         print("branch:it")      
# # class exam (Student):
# #     def subject(self):
# #         print("subject1: maths")
# #         print("subject2: dbms")
# #         print("subject3: c-lan")
# # obj=exam()
# # obj.college_name()
# # obj.student_info()
# # obj.subject()       

# #multiple inheritance
# class Subjmarks:
#     math=int(input("Enter marks of math subject"))
#     c=int(input("Enter marks of c subject"))
#     eng=int(input("Enter marks of eng subject"))
# class pracmarks:
#     cprac =int(input("Enter marks of cpractical"))
# class result(Subjmarks,pracmarks):
#     def total(self):
#         if self.math>=40 and self.c>=40 and self.eng>=40 and self.cprac>=20:
#             print("student is passed")
#         else:
#             print("student is failed")
# obj=result()
# obj.total()



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
       print("Name",self.name) 
       print("age",self.age) 
       print("rollno",self.rollno) 
p_obj=Student("shraddha",30,101)
p_obj.display()

class Animal:
    def eat(self):
        print("Animal is eating")
        
class Dog(Animal):
    # super().eat()
    def bark(self):
        print("Dog is barking")
d_obj=Dog()
d_obj.eat()
d_obj.bark()


class Bankaccount:
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance
class Savingaccount(Bankaccount):
    def __init__(self,accountnumber,balance,rateofinterest):
        self.rate=rateofinterest
        super().__init__(accountnumber,balance)
    def display(self):
        print("account number is",self.accountnumber)  
        print("Balance is" , self.balance)
        print("rate of interest",self.rate)
obj=Savingaccount(102,4000,6) 
obj.display() 

class Person:
    def __init__(self,name):
     self.name=name
class Employee(Person):
    def __init__(self,name,salary):
     self.salary=salary
     super().__init__(name)
class Manager(Employee):
    def __init__(self,name,salary,dept):
      self.dept=dept
      super().__init__(name,salary)
    def display(self):
        print("name of person",self.name)
        print("Salary of Employee",self.salary)
        print("department of manger",self.dept)     
m_obj=Manager("shradha",300000,"it") 
m_obj.display()         


class Add:
    def add(self,a,b):
        return a+b
class Sub:
    def sub(self,a,b):
        return a-b
class calculator(Add,Sub):
    pass
c_obj=calculator()
print("Addition:",c_obj.add(10,20))
print("Substraction:",c_obj.sub(40,23))