
def division(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test case
print(division(10, 2))  # Expected output: 5.0
print(division(15, 3))  # Expected output: 5.0