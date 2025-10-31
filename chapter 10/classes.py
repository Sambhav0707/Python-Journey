'''
so the classes are a blueprint for an object 
'''

class Car:
    def __init__(self , brandName , maxSpeed):
        self.brandName = brandName
        self.maxSpeed = maxSpeed # by this we initiallises the attributes of the class
    
    def getFullName(self):
        print(f"the full name of the car is :- {self.brandName}")


#creating and object of this class 

carObj = Car("Ferrari" , 200)

carObj.getFullName()

    