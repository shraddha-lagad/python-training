#membership operator
# 1. in  2. not in
# name = "help4code"
# print("h" in name)
# print("z" in name)
# print("z" not in name)


# for loop

# #for(initializing; condition; ince/dec)
for i in range(1,11,): #i=0
    print(2*i)


# for i in range(1,11): #i=0
#     print(2*i," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print("-----------------------------------------------------------------------------------------")

# for j in range(1,11):
#     print(11*j," ",j*12," ",j*13," ",j*14," ",j*15," ",j*16," ",j*17," ",j*18," ",j*19," ",j*20)

# list3 = [10,20,30,40,50]
# for i in list3:
#     print(i)

list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for x in list:
    sum=sum+x
print("The sum=",sum)

mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This is  My purchased cart item")
        break
    print(i)


# count = 0 
# for i in range(9):
#     if i%2==0:
#         print(i)
#     else:
#         print(i)
#         count +=1
# print("count =", count)

# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x == 2 or x == 4 or x == 6 or x == 8 or x==10:
#         print("even no is found",x)
#         break


# day = input("enter a day")
# if day == "saturday" or day =="SATURDAY" or day == "sunday" or day =="SUNDAY":
#     print("weekend")
# else:
#     print("working day")


# print(3/2)


# num = 123 #123
# a = num % 10 #a=3
# num = num // 10 #num= 12
# b = num % 10 #b=2
# c = num // 10 #c=1
# rev = a*100 + b*10 + c*1 #300+20+1
# print("reverse =",rev) 


# num = 1234567 #7654321
# a = num % 10 # a = 7
# num = num // 10 #num = 123456
# b = num % 10 #b=6
# c = num // 10 #c=12345
# d= num % 10

# print(d)

# Amount = int(input("please enter amount for withdraw"))
# print("100 notes =",Amount//100)
# print("50 notes= ",(Amount % 100)//50)
# print("20 notes= ",((Amount%100)%50)//20)
# print("10 notes= ",(((Amount%100)%50)%20)//10)
# print("5 notes= ",((((Amount%100)%50)%20)%10)//5)
# print("2 notes= ",(((((Amount%100)%50)%20)%10)%5)//2)
# print("1 notes= ",((((((Amount%100)%50)%20)%10)%5)%2)//1)

#write a prog to accept three age and check max age and print
# age1 = int(input("enter age 1 :"))
# age2 = int(input("enter age 2 :"))
# age3 = int(input("enter age 3 :"))
# if age1 > age2:
#     if age1 > age3:
#         print("age1 is greater",age1)
#     else:
#         print("age3 is greater",age1)
# else:
#     if age2 >age3:
#         print("age2 is greater",age2)
#     else:
#         print("age3 is greater",age3)

#WAP to accept any one character and check the entered character is UPPER CASE, LOWER CASE, DIGIT , SPECIAL SYMBOL so print msg with respect to the entered character.

# b= input("enter any one character:")

# if 'A' <= b <= 'Z':
#     print("entered character is an uppercase letter.")
# elif 'a' <= b <= 'z':
#     print({''})


# ch = ord(input("enter any character")) #0=48

# #ord function used to convert in ASCII code
# if ch>=65 and ch<=91: #A=65
#     print("your entered character is in upper case")
# elif ch>=97 and ch<=122:
#     print("your entered character is in lower case")
# elif ch>=48 and ch<=57:
#     print("your entered character is digit")
# else:
#     print("your entered character is in special symbols")


# username = input("Enter Username:")
# password = input("Enter password:")
# if username == password:
#     print("Login successful")
# else:
#     print("invalid password")



# while True:
#     username = input("Enter Username:")
#     password = input("Enter password:")
#     if username == password:
#         print("Login successful") 
#         break
#     else:
#         print("Invalid login")


# s = "help4code is a best platrform for pacticing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find('programming'))

#fing() return starting index no of string if it is found else if string doesnt exist then it return -1.
#-----------------------------------------------------------------------------------------------------------

# s = "prashant","ashish","sandip"
# m = '|'.join(s)
# print(m)


# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('Subject Marks :')
# phy = 60
# chem = 50
# math = 70
# print("physics={} chemistry={} Math={}".format(phy,chem,math))
# print("physics={0} chemistry={1} math={2}".format(phy,chem,math))
# print("physics ={x} chemistry ={y} math ={z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("total marks""{total}")
# print("Roll No=","7".zfill(4)) 


#user defined logic 

# name = "help4code"
#        #012345678
# for i in name:
#     print(i)


# name = "prashant"
# i=0  #3
# for x in name: #2:a
#     if x == 'n':
#         print("The character present at index no. ",i," value=:",x)
#         break
#     i=i+1 #update by one


# a = "shiwaleew"
# for i in a:
#     if i =='w':
#         print(i)



# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)

#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) #160
# print((a-b)*(c/d)) #40
# print(a+(b*c)/d) #110


#removing spaces from the string
#1. rstrip()===>To remove spacesat right hand side
#2. lstrip()===>To remove spaces at left hand side
#3. strip()===>To remove spaces both side
# city=input("enter you city name")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("hllo hyderabadi..adab")
# elif scity=='Chennai':
#     print("hello madrasi...vanakkam")
# elif scity=='Banglore':
#     print("hello kannadiga...shubhodaya")
# else:
#     print("your entered city is invalid")


