#Python program that uses recursion to compute the factorial of a number 
def factorial(n):
    # Base cases
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

def main():
    try:
        # Get input from user
        num = int(input("Enter a positive integer: "))
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
        