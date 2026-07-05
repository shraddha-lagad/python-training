# mylist = ["prashant","Ashish","KOmal","ankush","Ashish",77,"sandip",60.52,"sushhant"]
# # print(mylist)
# # print(type(mylist))
# # print(mylist[1])
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[-1]) #index last
# # print(mylist[2:5])
# # print(mylist[:5])
# # print(mylist[1:])
# # print(mylist[1:8:2])

# if "anskush" in mylist:
#     print("yes ankush is available")
# else:
#     print('not available')
# mylist.append('harsh')
# mylist.append("laxman")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy() #cloning
# print(newlist)

# mytuple = ("prashant","Ashish","rahul","sandip",)

# mylist = [['prashant','jha'] , [85.56],[440022,"yyy"]]
# print("example of multidimentional list:")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1=["prashant","jha"]
# # print(list1*2)

# list2=[50,25.50]
# print(list1+list2)

# list2=[50,25.50,'prashant']
# del list2[2]
# del list2
# # print(list2)

# list2=[50,25.50,'prashant']
# list2.clear()
# print(list2)

# name = "prashant" #str
# print(name)
# myname=list(name) #typecasting
# print(myname)
# # we have used list constructor

# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

#sorting example 
# mylist=[44,22,77,0,9,88]
# mylist.sort(reverse=True) #reverse=true
# print(mylist)

# mylist=[44,22,77,0,9,88]
# mylist.sort() # ascending order
# print(mylist)
# default sorting order for number is ascending order
# default sorting order for string is alphabetical
# we should know that list should contain homogeneous
# data otherwise will get type error
# python2 first short number then string follow

# Alising
#alising means assinging 


# mylist = [44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="prashant"
# print(mylist)
# print(newlist)



#Dictionary
# myDict={
#     101:"Prashant",
#     102:"ashish",
#     "103":"mogini",
#     "104":"trivani", #string
#     101:"ashish",
#     104:"ashish" #int
# }
# print(myDict)
# print(type(myDict))
# a=myDict[102] #extract value
# print(a)

# myDict[102]="peter" # replace old vallue by new value
# print(myDict)

# for x  in myDict:  # only print key 
#     print(x)
    
# for x in myDict.values(): #only print values
#     print(x)
    
# for x,y in myDict.items(): # printing both key and value
#     print(x,y)
    
# myDict["mobile_no"]= 256787643
# print(myDict)

# mydict={
#     101:"prashant",
#     "professional":"Devloper",
#     "empid":1001
# }
# # mydict.pop(101) #pop() method remove pair by specific key name
# # print(mydict)

# newdic=mydict.copy()
# print(newdic)


