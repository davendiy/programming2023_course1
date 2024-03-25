"""######### MatLang version 0.9, March 2024 ######### 

Іграшковий консольний інтерпретатор для математичних виразів. 

Додаткові функції: 
----------------
`exec(filename)` :
    відкрити файл з розширенням '.mlg' і виконати його як окрему програму

`clear()` : 
    очистити пам'ять 

`help()` : 
    показати це повідомлення 

`exit()` : 
    вийти

`print(variable)` : 
    показати значення змінної 
"""


from code_generator import generate_code
from interpreter import execute, ERRORS
from storage import clear, get_last_error, get


def show_help(): 
    print('\n')
    print(__doc__)


def exec_program(filename): 
    if not filename.endswith('.mlg'): 
        print('Помилка під час генерації коду: неправильне розширення у файлу.')
        return 
    
    with open(filename, 'r') as file: 
        lines = [line.strip() for line in file.readlines()]
        print('... ', end='')
        print(*lines, sep='\n... ')
        code, error = generate_code(lines, clear_storage=True)
        if error: 
            print('Помилка під час генерації коду:', error)
            return 
    
        last_error = execute(code)
        if last_error:
            error = ERRORS[last_error]
            print("Помилка виконання програми: {}".format(error))
            return 
    

def print_var(variable): 
    var = get(variable)
    if get_last_error() != 0: 
        print('Помилка під час виконання програми: змінна не існує.')
    else: 
        print(var)


def exec_line(line): 

    code, error = generate_code([line, ], clear_storage=False)
    if error: 
        print('Помилка під час генерації коду:', error)
        return 
    
    last_error = execute(code)
    if last_error:
        error = ERRORS[last_error]
        print("Помилка виконання програми: {}".format(error))
        return 
    

def mainloop(): 
    print(__doc__.splitlines()[0])
    print('\nВведіть `help()` для показу документації.')
    while True: 
        line = input('\n--> ').strip()

        if line == 'exit()': 
            break 
        elif line == 'help()': 
            show_help()
        elif line == 'clear()': 
            clear() 
        elif line.startswith('exec'): 
            filename = line[len('exec('):-1]
            exec_program(filename)
        elif line.startswith('print'): 
            variable = line[len('print('):-1]
            print_var(variable)
        else: 
            exec_line(line)

    
if __name__ == '__main__': 
    mainloop()
