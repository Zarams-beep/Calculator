import math

class Calculator:
    def __init__(self):
        pass
    
    def add(self, *args):
        return sum(args)
    
    def sub(self, *args):
        first_value = args[0]
        for i in args[1:]:
            first_value -= i
        return first_value
    
    def multiply(self, args):
        return math.prod(args)

    
    def divide(self, args):
        first_value = args[0]
        for i in args[1:]:
            first_value /= i
        return first_value 

    def mod_number(self, args):
        first_value = args[0]
        for i in args[1:]:
            first_value %= i
        return first_value

def calculator():
    calc = Calculator()
    dict_calculate = {'+': calc.add, '-': calc.sub, '*': calc.multiply, '/': calc.divide, '%': calc.mod_number}

    total = float(input('Enter number:'))
    continue_calculator = 'n'

    while True:
        print(f'Total: {total}')

        print(dict_calculate.keys())
        signs = input('Choose sign: ')
        
        sNum = float(input('Enter number: '))

        total = dict_calculate[signs](total, sNum)

        print(f'Result: {total}')

        continue_calculator = input('Continue calculator? (y/n): ').lower()
        if continue_calculator == 'n':
            break

calculator()
