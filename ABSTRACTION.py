# from abc import ABC ,abstractmethod
# class Helpmethod(ABC):
#     @abstractmethod   #abstrac class
#     def training(self):
#        pass
#     @abstractmethod   #abstract methood
#     def placement(self):
#        pass
# class Ashish(Helpmethod):
#     def training(self):
#        print('C,C++,JAva')
    
#     def placement(self):
#        print('JAVA PLACEMENT')
# class Ankush(Helpmethod):
#     def training(self):
#        print('python | django')
    
#     def placement(self):
#        print('python PLACEMENT')
# class Prashant(Helpmethod):
#     def training(self):
#        print('Machine learning')
    
#     def placement(self):
#        print('data science PLACEMENT')      
# obj1=Ashish()
# obj1.training()
# obj1.placement()

# obj2=Ankush()
# obj2.training()
# obj2.placement()

# obj3=Prashant()
# obj3.training()
# obj3.placement()


# from abc import ABC ,abstractmethod
# class Irctc(ABC): #abstrac base class
#     @abstractmethod   
#        #abstract methood
#     def Bookticket(self):
#        pass
# class Makemytrip(Irctc):
#     def Bookticket(self):
#        print("Welcome to makemytrip.com")
#        self.source= input("Enter source station name")
#        self.destination =input("Enter destination name")
#        self.date= input("Enter date")
# class Goibiob(Irctc):
#     def Bookticket(self):
#       print("welcome to Goibob")       
# class Yatra(Irctc):
#     def Bookticket(self):
#       print("Wlcome to yatra.com")
# obj1=Yatra()
# obj1.Bookticket()
# obj2=Makemytrip()
# obj2.Bookticket()
# obj3=Goibiob()
# obj3.Bookticket()

# class Arithmetic:   # method overodding
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c) 
# obj=Arithmetic()
# obj.add(10)
# obj.add(10,20)  
# obj.add(10,20,30) 

# class Rbi:  #Runtime polymorphism
#     def homeloan(self):
#         print("Home loan ratebof interest 8%")
#     def carloan(self):
#         print("car loan rate of interest 7%")
# class sbi(Rbi):
#     def homeloan(self):
#         print("home loan rate of interest 10.4%")
#         super().homeloan() # parent class ke property access karneke liye use kiya 
# sbiobj=sbi()
# sbiobj.homeloan()
# sbiobj.carloan()

#constructor overrideing
class Father:
    def __init__(self) :
        print("Father:- i am on time at breakfast table")
class child(Father):
    def __init__(self):
        print("child :- i will be late for breakfast")
        super().__init__()   # THIS WILL PRINT PARAENT CLASS MSG
obj=child()
