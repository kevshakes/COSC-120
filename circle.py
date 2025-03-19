#Python Program to Calculate Area and Circumference of a Circle

#import the pi constant
from math import pi 

#Get the radius from the user 
radius=float(input("Enter the radius:"))
#Calculate the Area
area=float(pi*radius*radius)
#Calculate the circumference 
circumference=float(2*pi*radius)
#Output the Area and Circumference 
print("Area of Circle:",area)
print("Circumference of Circle:",circumference)
