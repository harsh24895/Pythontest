import random


class Person():
    def __init__(self, name, age, health):
        self.name=name
        self.age=age
        self.health=health

    def intro(self):
        print("Enter the name {} and {}".format(self.name,self.age))

    def motion(self):
        ages = random.randrange(1,4)
        if ages == 1:
            print("this is good {}".format(self.name))
        elif ages == 2:
            print("this is average{}".format(self.name))
        else:
            print("not good so far".format(self.name))

    def healthissue(self):
        if self.health >= 80:
            print("Good heath {}".format(self.name))
        elif self.health <= 50:
            print("Good heath {}".format(self.name))
        elif self.health == 40:
            print("average {}".format(self.name))
        else:
            print("no issues need to work on")


ManTester = Person("tester","good",80)
ManTester.healthissue()
ManTester.motion()


class ChilhPerson(Person):
    def __init__(self,lastname,name, age, health):
        super().__init__(name,age,health)
        self.lastname=lastname


    def introdue(self):
        print("you are mortal")

    def defencee(self, other):
        if self.lastname=="rock":
            other.health -=10
        print(other.health)

    def result(self,other):
        if other.health <= 80:
            print("{} you are week now".format(other.name))

Ben = ChilhPerson('rock',80,'rock','east')
Ben.defencee(ManTester)