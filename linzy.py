def calculate_square_area_perimeter(side) : 
    side * side
    perimeter = 4 * side
    return area, perimeter

def calculate_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def calculate_circle_area_perimeter(radius):
    import math
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculate_triangle_area_perimeter(base, height, side1, side2):
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    return area, perimeter

def main():
    print("Choose an option:")
    print("1: Calculate area and perimeter of square and rectangle")
    print("2: Calculate area and perimeter of circle")
    print("3: Calculate area and perimeter of triangle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1: Calculate for square")
        print("2: Calculate for rectangle")
        sub_choice = int(input("Enter your choice: "))
        if sub_choice == 1:
            side = float(input("Enter the side length of the square: "))
            area, perimeter = calculate_square_area_perimeter(side)
        elif sub_choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area, perimeter = calculate_rectangle_area_perimeter(length, width)
        else:
            print("Invalid choice")
            return
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        area, perimeter = calculate_circle_area_perimeter(radius)
    elif choice == 3:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the length of the first side of the triangle: "))
        side2 = float(input("Enter the length of the second side of the triangle: "))
        area, perimeter = calculate_triangle_area_perimeter(base, height, side1, side2)
    else:
        print("Invalid choice")
        return

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

if __name__ == "__main__":
    main()