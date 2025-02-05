from calculator import display_menu, calculate

print('ARITHMETIC CALCULATOR\n')

def main():
    name = input('Enter your name: ')
    
    while True:
        display_menu()
        choice = input('\nSelect operation (1-5): ')
        
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Invalid input! Please enter numbers only.')
            continue
        
        result = calculate(choice, num1, num2)
        print(f'\n{result}' if result else 'Invalid selection!')
        
        if input('\nContinue? (y/n): ').lower() != 'y':
            break
    
    print(f'\n{name}, thank you for using this program!')

if __name__ == "__main__":
    main()
