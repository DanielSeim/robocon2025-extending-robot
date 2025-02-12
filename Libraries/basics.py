from robot.api.logger import write

def simple_keyword():
    print('Hello!')

def one_argument(name):
    print(f'Hello, {name}!')

def default_values(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

def should_be_positive(number: int|float):
    if number <= 0:
        raise AssertionError(f'{number} is not positive')
    
def log_using_print():
    print('Hi from print!')
    print('*INFO* Hi with explicit INFO level!')
    print('*DEBUG* Hi, debug!')

def log_using_api():
    write('Hi from API - Info!', 'INFO', False)
    write('Hi from API - Debug!', 'DEBUG', False)