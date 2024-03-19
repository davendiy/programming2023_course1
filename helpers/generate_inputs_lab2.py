import random


def random_rational(): 
    m = random.randint(-100, 100)
    while (n := random.randint(-100, 100)) == 0: 
        pass 

    res = ''
    if random.random() > 0.5: 
        res += ' '
    res += str(m)
    if random.random() > 0.5: 
        res += ' '

    res += '/'
    if random.random() > 0.5: 
        res += ' '
    res += str(n)
    if random.random() > 0.5: 
        res += ' '

    return res 


def random_integer(): 
    m = random.randint(-100, 100)
    res = ''
    if random.random() > 0.5: 
        res += ' '
    res += str(m)
    if random.random() > 0.5: 
        res += ' '
    return res 


def random_number(): 
    if random.random() > 0.5: 
        return random_rational()
    else: 
        return random_integer()


def random_poly():
    degree = random.randint(1, 20) 
    if random.random() > 0.1: 
        res = ','.join([random_number() for _ in range(degree)])
    else: 
        res = ','.join([random_integer() for _ in range(degree)])
    return res 


if __name__ == '__main__': 
    
    random.seed(42)

    for _ in range(10): 
        print(random_rational())

    for _ in range(10): 
        print(random_integer())

    for _ in range(10): 
        print(random_poly())

    with open('materials/semestr2/hw2/input1.txt', 'w') as file: 
        for _ in range(10_000): 
            file.write(random_number())
            file.write('\n')
    
    with open('materials/semestr2/hw2/input2.txt', 'w') as file: 
        for _ in range(10_000): 
            file.write(random_poly())
            file.write('\n')
    