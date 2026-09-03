"""
Program to calculate the factorial of a number.
Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1
"""


def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Calculate factorial using a loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {num} (recursive) = {factorial_recursive(num)}")
    print(f"Factorial of {num} (iterative) = {factorial_iterative(num)}")
