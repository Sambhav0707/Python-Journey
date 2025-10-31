l = ["sambhav" , "vaibhav" , "kairav" , "av"]


def rev(list , word):
    n = []
    for w in list:
        if not w == word:
            n.append(w.strip(word))

    return n

print(rev(l , "av")) 


class Employee:
    name = "Sambhav"
    age = 22

    def __init__(self):
        print("Init method")
    
    def getName(self):
        print(f"the name is {self.name}")

 
e1 = Employee()

e1.getName()

e1.name = "Sambhav Dalal"

e1.getName()



            

    
