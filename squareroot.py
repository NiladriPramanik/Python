def square_root(number, epsilon=1e-6):
   
    guess = number / 2  # Initial guess
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2

    return guess


# Example usage
number = float(input("Enter a number: "))
sqrt = square_root(number)
print(f"The square root of {number} is approximately {sqrt}")
