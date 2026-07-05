# import sys
# def add():
#     a= int(input("value of A"))
#     b= int(input("value of B"))
#     print(a+b)

# def sub():
#     a= int(input("value of A"))
#     b= int(input("value of B"))
#     print(a-b)

# def div():
#     a= int(input("value of A"))
#     b= int(input("value of B"))
#     print(a/b)
    
# def mult():
#     a= int(input("value of A"))
#     b= int(input("value of B"))
#     print(a*b)
# while True:
#     print("1, Addition")
#     print("2, substraction")
#     print("3, division")
#     print("4, multiplication")
#     print("Exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         add() 
#     elif choice==2:
#         sub() 
#     elif choice==3:
#         div() 
#     elif choice==4:
#         mult()
#     elif choice==5:
#         sys.exit()
        
        
    #stack implementation
# import sys
# class Stack:
#     def __init__(self,stacksize) :
#         self.stacksize=stacksize #stackssize defined
#         self.mystack=[] #list rep stack
#         print("stack has created")
    
#     def isFull(self):
#          if len(self.mystack)==self.stacksize:
#           return True
#          else:
#           return False  
#     def push(self,value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.mystack.append(value) 
#     def isEmpty(self):
#          if self.mystack==[]:
#              return True
#          else:
#              return False
                 
#     def display(self):
#         if self.isEmpty():
#             print("stsck is empty")
#         else:
#             print("stack =",self.mystack)
            
#     def pop(self):
#          if self.isEmpty():
#              print("Stack is empty")
#          else:
#              print(self.mystack.pop())
             
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.mystack[-1])
            
#     def delete(self):
#         # self.mystack= none
#          del self.mystack       
# size = int(input("Enter the size of stack:"))
# obj=Stack(size)
# while True:
    
#     print("1.Push")
#     print("2.display")
#     print("3.pop")
#     print("4.peek")
#     print("5.delete")
#     print("6.exit")
#     choice=int(input("Enter your choice:-"))
#     if choice==1:
#         value=int(input("Enter the value to push in stack"))
#         obj.push(value)
#     elif choice==2:
#         obj.display()
#     elif choice==3:
#         obj.pop()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.delete()
#     elif choice==6:
#         sys.exit()
        
        

import sys
class Queue:
    def __init__(self,queuesize) :
        self.queuesize=queuesize
        self.myqueue=[]
        
    def isFull(self):
        if len(self.myqueue)==self.queuesize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.myqueue==[]:
            return True
        else:
            return False
    
    def enQueue(self,value):
        if self.isFull():
          print("Queue is full")
        else:
          self.myqueue.append(value)  
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myqueue)
            
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myqueue.pop(0))
            
    def frontpeek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myqueue[0])  #it return first element
    
    def delete(self):
        del self.myqueue
    
size=int(input("enter the size of Queue:"))
queobj=Queue(size)

while True:
    print("1.Enqueue")
    print("2.Display")
    print("3.Dequeue")
    print("4.frontPeek")
    print("5.Delete Queue")
    print("6.Exit")
    chioce=int(input("Enter Your choice:"))
    if chioce==1:
        value=int(input("Enter value to add in Queue: "))
        queobj.enQueue(value) 
    elif chioce==2:
        queobj.display()
    elif chioce==3:
        queobj.deQueue()
    elif chioce==4:
        queobj.frontpeek()
    elif chioce==5:
        queobj.delete()
    elif chioce==6:
        sys.exit()
    
    