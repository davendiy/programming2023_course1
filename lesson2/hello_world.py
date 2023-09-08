name = input("Введіть своє ім'я.\n--> ")

print('Привіт', name)

age = int(input("Скільки вам років?\n--> "))

print(f"Вам {age} років.")

print(f"Вам приблизно {age * 365} днів.")

first_dig = age // 10 
second_dig = age % 10 
