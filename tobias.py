#oppop
print("Choose any of the three options")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area andperimeter of a rectangle")
choice=int(input("choose among the choices :"))
from math import pi
if choice ==1:
    radius=float(input("enter radius of the circle"))
    area=float(pi*radius*radius)
    circumference=float(2*pi*radius)
    print("area of a circle",area)
    print("circumference of a circle",circumference)
elif choice ==2:
    base=float(input("enter the baseof the triangle"))
    height=float(input("enter the height of the triangle"))
    hypotenuse=float(input("enter the hypotenuseof the triangle"))
    area=float(0.5*base*height)
    perimeter=(base+hypotenuse+hypotenuse) #perimeter of a triangle is the sum of the three sides not the base and hypotenuse only
    print("area of a triangle",area)
    print("perimeterof the triangle",perimeter)
elif choice==3:
    width=float(input("enter the width of the rectangle"))
    length=float(input("enter the length of the rectangle"))
    area=float(width*length)
    perimeter=float(width+length+width+length)
    print("area of rectangle",area)
    print("perimeter of rectangle",perimeter)
else:
    print("invalid option choose 1, 2 or 3")