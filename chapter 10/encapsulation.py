# encapsulation :- it is privatising the data within a class 

class Car:
    def __init__(self , brandName , model):
        self.__brandName =  brandName
        self.model = model

    def get_brandName(self):
        return self.__brandName
    def set_brandName(self, newbrandName):
        self.__brandName = newbrandName
    

car = Car("Suzuki" , "Swift")

print(car.get_brandName())

car.set_brandName("Maruti")

print(car.get_brandName())


