# This script takes two numbers as input from the user and prints their sum

def main():
    while True:
        try:
            # Taking two numbers as input from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Calculating the sum
            result = num1 + num2

            # Printing the result
            print(f"The sum of {num1} and {num2} is {result}")
            break  # Exit the loop after successful input
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()