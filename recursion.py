#factorial 
# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4)) #4*factoral(3) 
#                       #3*factoral(2)
#                       #2*factoral(1)
# # palindrome
# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0]!=string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome('tacocat'))

# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent)
# print(power(2,4)) #4   # 2*(2,1) 2*(2,0) 2*(2,1) 2*2*1 4
# print(power(2,0)) #1

# def productOfArray(arr): #(2,3)
#     if len(arr)==0:                            
#         return 1
#     return arr[0]*productOfArray(arr[1:]) #1*(2,3)
# print(productOfArray([1,2,3])) #6

# def recursiveRange(num):
#     if num<=0:
#         return 0
#     return num+recursiveRange(num-1)
# print(recursiveRange(5))

def fib (num):
    if(num<2):
        return num
    return fib(num-1)+fib(num-2)
print(fib(4))