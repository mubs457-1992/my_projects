"""
Calculator module with basic arithmetic operations
"""

class Calculator:
    """Simple calculator class with basic operations"""
    
    def __init__(self):
        """Initialize calculator"""
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers"""
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
    
    def modulo(self, a, b):
        """Get remainder of division"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a % b
        return self.result
    
    def power(self, a, b):
        """Raise a to the power of b"""
        self.result = a ** b
        return self.result
    
    def square_root(self, a):
        """Calculate square root"""
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        self.result = a ** 0.5
        return self.result
    
    def clear(self):
        """Clear the result"""
        self.result = 0
        return self.result
    
    def get_result(self):
        """Get the current result"""
        return self.result

