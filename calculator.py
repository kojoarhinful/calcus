def display_menu():
    """Display the arithmetic operations menu"""
    print('\nMenu')
    print('^^^^')
    print('1. Addition')
    print('2. Multiplication')
    print('3. Subtraction')
    print('4. Modulus')
    print('5. Average')

def calculate(operation, fnum, snum):
    """Perform calculation based on selected operation"""
    operations = {
        '1': ('Addition', lambda a, b: a + b),
        '2': ('Multiplication', lambda a, b: a * b),
        '3': ('Subtraction', lambda a, b: a - b),
        '4': ('Modulus', lambda a, b: a % b),
        '5': ('Average', lambda a, b: (a + b) / 2)
    }
    
    if operation not in operations:
        return None
    
    op_name, func = operations[operation]
    try:
        result = func(fnum, snum)
        return f"{op_name} result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except Exception as e:
        return f"Error: {str(e)}"
