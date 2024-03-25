# Define a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base case: if n is 1 or 2, return 1 (F1 and F2 are both 1)
    if n == 1 or n == 2:
        return 1
    else:
        # Recursive case: calculate the nth Fibonacci number by adding the previous two
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input for the desired term (n)
n = int(input("Enter a positive integer (n) to find the nth Fibonacci term: "))

# Check if n is a valid positive integer
if n <= 0:
    print("Please enter a valid positive integer.")
else:
    # Calculate and print the nth Fibonacci term
    result = fibonacci(n)
    print(f"The {n}th Fibonacci term is: {result}")
