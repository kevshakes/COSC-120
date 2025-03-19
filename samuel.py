import math

def calculate_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")

def calculate_triangle():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area of the triangle: {area:.2f}")
    print(f"Perimeter of the triangle: {perimeter:.2f}")

def calculate_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of the rectangle: {area:.2f}")
    print(f"Perimeter of the rectangle: {perimeter:.2f}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Calculate area and circumference of a circle")
        print("2. Calculate area and perimeter of a triangle")
        print("3. Calculate area and perimeter of a rectangle")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            calculate_circle()
        elif choice == '2':
            calculate_triangle()
        elif choice == '3':
            calculate_rectangle()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()