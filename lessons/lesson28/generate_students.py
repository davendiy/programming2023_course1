
import random
from tqdm import tqdm 
import os 
from string import ascii_lowercase

from pipeline_v1 import Student


def get_random_student(): 
    
    name = random.choice(['Name', 'David', 'Volodymyr', 'Cat', 'Julia'])
    n = random.randint(4, 15)
    surname = ''
    for _ in range(n):
        surname += random.choice(ascii_lowercase)
    year = random.randint(1999, 2005)
    salary = 2500 + 100 * random.random()
    return Student(name, surname, year, salary)


def generate_file(filename, n=1_000_000): 
    with open(filename, 'w') as file: 
        for _ in tqdm(range(n)): 
            st = get_random_student()
            print(st.name, st.surname, st.year, st.salary, sep=',', file=file)


if __name__ == '__main__': 
    cur_dir = os.path.abspath(__file__)
    cur_dir = os.path.split(cur_dir)[0]

    generate_file(cur_dir + '/test_file.txt', n=1_000_000)
