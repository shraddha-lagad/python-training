# class Base:
#     def __init__(self):
#         print("parent class constructor called")
#         self.a ="parshant"  #public data member
#         self.__c ="Ashish"  #private member   THIS IS NOT ACCESSIBLE TO OTHER CLASS
# class Derived(Base):   #child class
#     def __init__(self):
#         Base.__init__(self)   # calling constructor of base class
#         print("calling private member of base class: ")
#         # print(self.a)
#         # print(self.__c)     # CHILD CLASS DO NOT ACCESS PARENT CLASS CHA PRIVATE MEMBER
# # obj1 =Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 =Base()
# print(obj2.a) #accessible
# print(obj2.__c) #not accessible




# class Base:
#     def __init__(self):
#         print("parent class constructor called")
#         self.a ="parshant"  #public data member
#         self._c ="Ashish"  #private member   THIS IS NOT ACCESSIBLE TO OTHER CLASS
# class Derived(Base):   #child class
#     def __init__(self):
#         Base.__init__(self)   # calling constructor of base class
#         print("calling private member of base class: ")
#         # print(self.a)
#         # print(self._c)     # CHILD CLASS DO NOT ACCESS PARENT CLASS CHA PRIVATE MEMBER
# obj1 =Derived()
# print(obj1.a)
# # print(obj1._c)
# # obj2 =Base()
# # print(obj2.a) #accessible
# # print(obj2._c) #not accessible
     


# class Login:
#     def __init__(self) :
#         self.__password="abcd@123"
#     def login(self,password):
#         if password==self.__password:
#           print("phone is unlocked ")  
#         else:
#             print("phone is locked")
# obj=Login()
# obj.login("abcd@123") 
# obj.login("abc@1234")
            
class Bank:
    def __init__(self,account,balanace,pin) :
        self.account=account
        self.__balance=balanace
        self.__pin=pin
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid amount ")
    def withdrawl(self,amount,pin):
        if pin==self.__pin:
         if self.__balance>=amount:
            self.__balance -=amount
         else:
            print("Not sufficcient balance")
        else:
            print("invalid pin")
    def account_detail(self):
        print("Account number:",self.account)
        print("Account balance:",self.__balance)
        print("Account pin:",self.__pin)
    def change_pin(self,old_pin,new_pin):
        if self.__pin == old_pin:
            self.__pin =new_pin 
        else:
            print("Old pin is not valid")
    
obj=Bank('A123',4000,234)
obj.deposit(4900)
obj.withdrawl(4800,234)
obj.change_pin(290,800)
obj.account_detail()               

class Company:
    def __init__(self,employee,salary):
        self.employee=employee
        self._salary=salary
    def AnnualSalary(self):
        self._asalary=self._salary*12
    def show(self):
        print("Employee name",self.employee)
        print("Salary",self._salary)  
        print("Annual salary",self._asalary) 
obj=Company("shraddja",1000)
obj.AnnualSalary()
obj.show()