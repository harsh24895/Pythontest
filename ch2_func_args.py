def user(name, gender, age=8, city="dester"):
    ''' This will print name gender, age, city'''
    # here is the way that we can print and initialize the variable and later call it ******This are called positional arguments*****
    print("{} is {} and {} years , from {}".format(name, gender, age, city))

user("Jan","Male","25","Des")


#***Keyword argument***** in here it will get the default argument whichever we have mention in method
user("rest","Male")


#**-- *args and **kwargs aguments in the python it will multiple number of arguments follwed by positional argument
def appli(user, test, *args, **kwargs):
    print("this is {} and {}. and his email".format(user, test))

appli("test52","second", email="skdjfnsf@gmail td")
