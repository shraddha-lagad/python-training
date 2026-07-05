#whenever we want to use data future so we used file handling concept
# f=open("myfile2.txt","a")
# print("name of file:",f.name)
# print("file mode:",f.mode)
# print("readable:",f.readable())
# print("writeable:",f.writable())
# print("file closed:",f.closed)
# f.close()
# print("file closed :",f.closed)

# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Banglore is a smart city")
# f.write("\n Nashik is a smart city")
# f.close()
# print("file opertion is done")

#inserting list
# f =open("newfile2.txt","w")
# mylist=["prashant","mahesh","suresh"]
# f.writelines(mylist)
# f.close()
# print("Written work has done sucessfullly")

# f=open("myfile2.txt","r")
# print(f.read())
# f.close()

# with open("myfile2.txt","w")as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("prashant\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)

# with open("myfile2.txt","r")as f:
#     content=f.read()
#     print(content)

# f1=open("cat.jpg","rb") #readbinary
# f2=open("photo.jpeg","wb") #writebinary
# data=f1.read() #it will read all binary info
# f2.write(data)

import csv
f=open("student.csv","a",newline="")
a=csv.writer(f) #it do write operation
a.writerow(["studentID","rollno","name","mobileno","m1","m2","m3","total","percentage","email"])  
studentid=int(input("Enter student id:"))
rollno=int(input("Enter rollno :"))
name=(input("Enter your name :"))
mobileno=int(input("Enter your mobile:"))
m1=int(input("Enter marks 1 : "))
m2=int(input("Enter marks 2 : "))
m3=int(input("Enter marks 3 : "))
email=input("Enter email")


print("Student record has save")
total=m1+m2+m3
print("tottal is",total)
percentage=total/3
print("percentage",percentage)
a.writerow([studentid,rollno,name,mobileno,m1,m2,m3,total,percentage,email,])
if m1>=40 and m2>=40 and m3>=40:
    print("pass")
else:
    print("fail")