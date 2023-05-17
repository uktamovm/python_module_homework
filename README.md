# Welcome to Python Module Homework

This repository contains a set of 10 tasks that involve using the `math` module. To complete the homework, follow the instructions below:

1. Fork this repository to your own GitHub account.
2. Solve each task by writing the required code.
3. Commit your solutions with appropriate commit messages.
4. Push the changes to your GitHub repository.
5. Submit the link to your repository for grading.

---

## Task 1: Square Root Calculation

Write a Python program that calculates the square root of a given number using the `math` module.

```python
# Calculate the square root of a number
import math

def calculate_square_root(number):
    return math.sqrt(number)

# Example usage
input_number = 16
result = calculate_square_root(input_number)
print(result)
```

---

## Task 2: Factorial Calculation

Write a Python program that calculates the factorial of a given number using the `math` module.

```python
# Calculate the factorial of a number
import math

def calculate_factorial(number):
    return math.factorial(number)

# Example usage
input_number = 5
result = calculate_factorial(input_number)
print(result)
```

---

## Task 3: Trigonometric Calculations

Write a Python program that calculates the sine, cosine, and tangent of an angle using the `math` module.

```python
# Perform trigonometric calculations
import math

def perform_trigonometric_calculations(angle):
    # Convert the angle to radians
    angle_radians = math.radians(angle)
    
    # Calculate the sine, cosine, and tangent of the angle
    sine = math.sin(angle_radians)
    cosine = math.cos(angle_radians)
    tangent = math.tan(angle_radians)
    
    return sine, cosine, tangent

# Example usage
input_angle = 45
sine, cosine, tangent = perform_trigonometric_calculations(input_angle)
print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)
```

---

## Task 4: Logarithm Calculation

Write a Python program that calculates the logarithm of a number to a specified base using the `math` module.

```python
# Calculate the logarithm of a number
import math

def calculate_logarithm(number, base):
    return math.log(number, base)

# Example usage
input_number = 100
input_base = 10
result = calculate_logarithm(input_number, input_base)
print(result)
```

---

## Task 5: Exponential Calculation

Write a Python program that calculates the exponential value of a number using the `math` module.

```python
# Calculate the exponential value of a number
import math

def calculate_exponential(number):
    return math.exp(number)

# Example usage
input_number = 2
result = calculate_exponential(input_number)
print(result)
```

---

## Task 6: Round to Nearest Integer

Write a Python program that rounds a decimal number to the nearest integer using the `math` module.

```python
# Round a decimal number to the nearest integer
import math

def round_to_nearest_integer(number):
    return round(number)

# Example usage
input_number = 3.7
result = round_to_nearest_integer(input_number)
print(result)
```

---

## Task 7: Ceiling and Floor Calculation

Write a Python program that calculates the ceiling and floor values of a number using the `math` module.

```python
# Calculate the ceiling and floor values of a number
import math

def calculate_ceiling_floor(number):
    ceiling = math.ceil(number)
    floor = math.floor(number)
    return ceiling, floor

# Example usage
input_number = 4.3
ceiling, floor = calculate_ceiling_floor(input_number)
print("Ceiling:", ceiling)
print("Floor:", floor)
```

---

## Task 8: Degree to Radian Conversion

Write a Python program that converts an angle from degrees to radians using the `math` module.

```python
# Convert an angle from degrees to radians
import math

def convert_degrees_to_radians(degrees):
    return math.radians(degrees)

# Example usage
input_degrees = 90
result = convert_degrees_to_radians(input_degrees)
print(result)
```

---

## Task 9: Radian to Degree Conversion

Write a Python program that converts an angle from radians to degrees using the `math` module.

```python
# Convert an angle from radians to degrees
import math

def convert_radians_to_degrees(radians):
    return math.degrees(radians)

# Example usage
input_radians = 1.5707963267948966
result = convert_radians_to_degrees(input_radians)
print(result)
```

---

## Task 10: Power Calculation

Write a Python program that calculates the power of a number using the `math` module.

```python
# Calculate the power of a number
import math

def calculate_power(base, exponent):
    return math.pow(base, exponent)

# Example usage
input_base = 2
input_exponent = 3
result = calculate_power(input_base, input_exponent)
print(result)
```

---

Once you have completed all the tasks, your homework will be ready for submission. Good luck!
