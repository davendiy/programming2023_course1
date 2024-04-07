"""
Нехай маємо файл. У файлі є якісь записи. 

Наприклад це будуть студенти.
"""

import os 
from typing import Iterable
from dataclasses import dataclass


@dataclass
class Student: 
    name: str
    surname: str
    year: int 
    salary: float 


def read_file(filename, sep=','): 
    with open(filename) as file: 
        for line in file: 
            student = line.strip().split(sep)
            student[2] = int(student[2])
            student[3] = float(student[3])
            student = Student(*student)
            yield student


def groupby(student_list: Iterable[Student], field='year'): 
    res = {}
    for el in student_list:
        group_value = getattr(el, field)
        if group_value not in res: 
            res[group_value] = []    
        res[group_value].append(el)
    
    for k, v in res.items(): 
        yield k, v


def max_field(student_list: Iterable[Student], field='salary'):
    return max(student_list, key=lambda x: getattr(x, field)) 


def mean(seq: Iterable[Student], field='salary'): 
    n = 0 
    res_mean = 0 
    for el in seq: 
        res_mean = res_mean * (n / (n + 1)) + getattr(el, field) / (n + 1)
        n += 1
    return res_mean


def median(seq: Iterable, field='salary'): 
    res = sorted(seq, key=lambda x: getattr(x, field))
    n = len(res)
    if n % 2 == 0: 
        return (getattr(res[n // 2 - 1], field) + getattr(res[n // 2], field)) / 2 
    else: 
        return getattr(res[n // 2], field)


def pipeline(filename, verbose=False):

    if verbose: 
        print('[*] Start reading file')

    student_list = read_file(filename)
    
    if verbose: 
        print('[*] Start groupby')
    student_dict = groupby(student_list, field='year')
    stud_salaries = {}

    if verbose: 
        print('[*] Start max field')
    for year, students in student_dict: 
        stud_salaries[year] = max_field(students, field='salary')

    if verbose: 
        print('[*] Start mean')
    mean_max_sal = mean(stud_salaries.values()) 

    if verbose: 
        print('[*] Start median')
    median_max_sal = median(stud_salaries.values())
    return mean_max_sal, median_max_sal


if __name__ == '__main__': 
    cur_dir = os.path.abspath(__file__)
    cur_dir = os.path.split(cur_dir)[0]

    filename = cur_dir + '/test_file.txt'

    print(pipeline(filename, verbose=True))
