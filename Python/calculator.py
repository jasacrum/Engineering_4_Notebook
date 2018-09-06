#PythonCalulator
#Written By Jacksper


def doMath(a,b):
    return a + b

def doMath(a,b,2):
    return a - b

def doMath(a,b,3):
    return a * b

def doMath(a,b,4):
    return a / b

def doMath(a,b,5):
    return a % b

a = (input("enter first number-"))
b = (input("enter second number-"))


print("Sum:\t\t" + doMath(a,b))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
