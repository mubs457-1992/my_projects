# Calculator Project

A simple yet functional calculator application built in Python with support for basic arithmetic operations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Modulo, power, and square root
- **Error Handling**: Validates input and handles edge cases (division by zero, negative square roots)
- **Interactive Menu**: User-friendly command-line interface
- **Result Storage**: Keep track of the last calculation result
- **Unit Tests**: Comprehensive test suite for all operations

## Project Structure

```
calculator/
├── calculator.py          # Main calculator module with Calculator class
├── main.py               # Interactive calculator application
├── test_calculator.py    # Unit tests for the calculator
└── README.md             # This file
```

## Files Description

### calculator.py
Contains the `Calculator` class with the following methods:
- `add(a, b)` - Addition
- `subtract(a, b)` - Subtraction
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division (with zero-check)
- `modulo(a, b)` - Modulo/remainder
- `power(a, b)` - Power/exponentiation
- `square_root(a)` - Square root (with negative number check)
- `clear()` - Clear the result
- `get_result()` - Get the current result

### main.py
Interactive calculator application that:
- Displays a menu with 10 options
- Takes user input for calculations
- Displays results
- Handles errors gracefully
- Allows continuous calculations

### test_calculator.py
Unit tests covering:
- All basic operations
- Edge cases (zero division, negative square roots)
- Result verification
- Error handling

## How to Use

### Running the Calculator

```bash
python main.py
```

This will start the interactive calculator with a menu-driven interface:

```
==================================================
SIMPLE CALCULATOR
==================================================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulo (Remainder)
6. Power
7. Square Root
8. View Result
9. Clear
0. Exit
==================================================
```

### Running Tests

```bash
python -m unittest test_calculator.py
```

Or with verbose output:

```bash
python -m unittest test_calculator.py -v
```

### Using Calculator as a Module

```python
from calculator import Calculator

calc = Calculator()

# Perform calculations
result = calc.add(10, 5)
print(f"10 + 5 = {result}")  # Output: 10 + 5 = 15

result = calc.multiply(4, 7)
print(f"4 * 7 = {result}")  # Output: 4 * 7 = 28

# Check the last result
print(calc.get_result())  # Output: 28

# Clear the result
calc.clear()
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## Examples

### Example 1: Basic Addition
```
Enter your choice (0-9): 1
Enter first number: 15
Enter second number: 7
15.0 + 7.0 = 22.0
```

### Example 2: Division with Error Handling
```
Enter your choice (0-9): 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

### Example 3: Power Operation
```
Enter your choice (0-9): 6
Enter first number: 2
Enter second number: 8
2.0 ** 8.0 = 256.0
```

## Future Enhancements

- GUI interface using tkinter or PyQt
- History of calculations
- Support for complex numbers
- Scientific calculator functions (sin, cos, log, etc.)
- Keyboard calculator input

## License

This project is free to use and modify.

## Author

Created as a simple calculator project for learning Python programming.
