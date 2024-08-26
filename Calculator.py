def add():
    a = float(input("enter the number"))
    b = float(input("enter the number"))
    print(a+b)
def sub():
    a = float(input("enter the number"))
    b = float(input("enter the number"))
    print(a - b)

def mul():
    a = float(input("enter the number"))
    b = float(input("enter the number"))
    print(a * b)

def div():
    a = float(input("enter the number"))
    b = float(input("enter the number"))
    print(a / b)


comp = input("enter the choose +,-,*,/")

if comp == "+":
    add()
elif comp == "-":
    sub()
elif comp == "*":
    mul()
elif comp == "/":
    div()
else:
    print("incorrect choose")


