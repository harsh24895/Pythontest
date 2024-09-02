
def addition():
    a = float(input("enter the data"))#here we are casting the data type float to a variable and taking the input
    b = float(input("enter the data of b"))
    print(a+b)

def subtraction():
    a = float(input("Enter the data of a:"))
    b = float(input("Enter the data of b:"))
    print(a-b)


def mul():
    a = float(input("enter the data"))
    b = float(input("enter the data"))
    print(a * b)
def div():
    a = float(input("enter the data"))
    b = float(input("enter the data"))
    print(a / b)

comp = input("choose any +,-,*,/")

if comp == '+':
    addition()
elif comp == '-':
    subtraction()
elif comp == '*':
    mul()
elif comp == '/':
    div()
else:
    print("incorrect choice")


