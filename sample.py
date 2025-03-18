def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    
    return factorial

def main():
    try:
        num = int(input("Enter a number to find its factorial: "))
        result = calculate_factorial(num)
        print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
