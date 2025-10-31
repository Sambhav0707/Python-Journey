class Calculator:
    def __init__(self , number:int):
        self.number = number
    
    
    def getSquare(self):
        n = self.number
        return (n*n)
    
    def getCube(self):
        n = self.number
        return (n*n*n)
    
    def getSqRoot(self):
        n = self.number
        return ((n) ** 0.5)
    
    @staticmethod   
    def greet():
        print("hello")

cal = Calculator(7)

cal.number = 4

print(cal.getCube())
print(cal.getSqRoot())
print(cal.getSquare())

cal.greet()