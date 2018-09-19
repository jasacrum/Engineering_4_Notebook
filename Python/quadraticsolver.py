# Quadratic Solver
# Created by Jacksper
import math


print("Quadratic Solver")
print("Enter the Coefficients for ax^2 + bx + c = 0")

a = int(input("Enter First Coefficient"))
b = int(input("Enter Second Coefficient"))
c = int(input("Enter Third Coefficient"))

def roots(a,b,c):
    x1 = (-b+math.sqrt(discriminate(a,b,c)))/(2*a)
    x2 = (-b-math.sqrt(discriminate(a,b,c)))/(2*a)
    arr = [x1,x2]
    return arr

def discriminate(a,b,c):
    d = ((b**2) - (4*a*c))
    return d

d = discriminate(a,b,c)

if d < 0:
    print("No real roots mate!")
else:
    print("Discriminate:\t" + str(discriminate(a,b,c)))
    print("Roots:\t" + str(roots(a,b,c)))


