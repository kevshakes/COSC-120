import math

def circle_calculations():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

def triangle_calculations():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    side3 = float(input("Enter the length of the third side of the triangle: "))
    area = 0.5 * base * height
    perimeter = side1 + side2 + side3
    print(f"Area of the triangle: {area:.2f}")
    print(f"Perimeter of the triangle: {perimeter:.2f}")

def rectangle_calculations():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")

def main():
    print("Choose an option:")
    print("1. Calculate area and circumference of a circle")
    print("2. Calculate area and perimeter of a triangle")
    print("3. Calculate area and perimeter of a rectangle")
    option = input("Enter your choice (1, 2, or 3): ")

    if option == '1':
        circle_calculations()
    elif option == '2':
        triangle_calculations()
    elif option == '3':
        rectangle_calculations()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()