from random import random


class Person():
  def __init__(self, firstname, lastname, health, status):
    self.firstname = firstname
    self.lastname = lastname
    self.health = health
    self.status = status

  def introduec(self):
    print("My name is {} {}".format(self.firstname, self.lastname))

  def emotion(self):
    emotional = random.randrange(1, 5)
    if emotional == 1:
      print(" this is good{}".format(self.firstname))
    elif emotional == 2:
      print("this is bad{}".format(self.firstname))

  def statuChange(self):
    if self.health == 100:
      print("this is great health {}".format(self.firstname))
    elif self.health <= 75:
      print("this is good health {}".format(self.firstname))
    elif self.health <= 50:
      print("this is Avg health {}".format(self.firstname))
    else:
      print("this is not well enough{}".format(self.firstname))


#here we just have assign the variable to the class with paramerters with three users
Tester1 = Person("test23", "test22222", 90, "test")
resting2 = Person("restingFirst", "resting", 40, "resting")
Tester3 = Person("Tester3", "firstname_", 85, "rest")

#here we just prinitng the variable with parameters
print("{} and {}".format(Tester1.firstname, Tester1.lastname))

Tester1.introduec()
resting2.introduec()

Tester1.statuChange()
resting2.statuChange()


class ChildClass(Person):

  def __init__(self, weapon, firstname, lastname, health,status):  #this is a constructor for ChildClass
    super().__init__(firstname, lastname, health, status) ##multiple inheretance
    self.weapon = weapon

  def introduce(self):
    print("You are the mortal enemy") # this polymerfizium as we are overrriding this method as parent class has the same name method

  def hurt(self, other):  # here "self" we are accessing the attribute of the class "ChildClass"
    if self.weapon == "rock":
      other.health -= 10  #here we are using the python decrement opertor "-="
    elif self.weapon == "stick":
      other.health -= 5
    print(other.health)

  def insult(self, other):  #for "other" it will access the attribute of the class "Person" for some reason
    if other.health <= 80:
      print("{} you are week now".format(other.firstname))

  def steal(self, other):
    print("good {}, we got the stuff".format(other.firstname))
    if other.status == True:
      other.stauts = False


Den = ChildClass('rock', 'peter', 'deter', 98, status=True)
Den.introduce()#this is childClass method overriding to see the result


Den.hurt(Tester1)  # here it will cut down the health of the Tester1 to -10.
Den.insult(resting2)  #this will get the firstname from another class and assign with childclass attributes
Den.insult(Tester3)

Den.steal(resting2)

###################
resting2.steal(Den)  #this will throuw an error as steal is not a method of the class Person
