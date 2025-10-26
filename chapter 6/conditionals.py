# if , else , elif


#write a program to determine the age is legal(>= 18) or not

age = int(input("enter the age:- "))

if(age >= 18):
    print("it is a legal age")

elif(age < 0):
    print("please enter a valid age")

else:
    print("age is not valid")    