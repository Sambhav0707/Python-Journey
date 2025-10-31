#inheritence is basically a class using functionality of its parent class 

class Bird:
    def fly(self,statement = "the bird can fly"):
        print(statement)


class Ostrich(Bird):
    def fly(self):
        super().fly("this bird cannot fly")


bird = Bird()

bird.fly()

ostrich = Ostrich()

ostrich.fly()