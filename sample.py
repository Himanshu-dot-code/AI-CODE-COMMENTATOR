def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class Calculator:
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

print(add(5, 3))
print(subtract(10, 4))

calc = Calculator()
print(calc.multiply(6, 7))
print(calc.divide(8, 2))
