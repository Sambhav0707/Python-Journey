#polymorphism :- same methods names performing diff task or functionality 



class Car:
    pass



class Suv(Car):
    def getInfo(self):
        print("this is SUV")



class Sadan(Car):
    def getInfo(self):
        print("this is Sadan")


vento = Sadan()

xuv500 = Suv()

vento.getInfo()

xuv500.getInfo()