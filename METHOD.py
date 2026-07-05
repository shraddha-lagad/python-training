class Rbi:
    #declaring public method
    def publicpolicy(self):
        print("check the public policy of Rbi")
        # declaring  private method
    def __privatepolicy(self):
        print("ther is some private policy which is not accessible by public")
class Sbi(Rbi):
    def __init__(self) :  #first sbi class const called
        Rbi().__init__()      #2nd parent class constructor called
    def callingPublicMethod(self):   #child class public method
        print("\n Inside child class")
        self.publicpolicy() #calling parent class public method
    def callingPrivateMethod(self) :
        self.__privatepolicy()
# obj1=Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicpolicy()
# obj1.__privatepolicy()
obj2=Rbi()
obj2.publicpolicy()
obj2.__privatepolicy()

