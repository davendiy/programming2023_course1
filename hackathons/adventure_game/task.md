# Adventure game 

Ви працюєте у маленькій геймінговій інді компанії. Ваша задача -- написати 
невелику пригодницьку гру з 10-ма рівнями з різними механіками. 
Так як ви інді компанія, у вас немає грошей на потужну команду дизайнерів, 
тому ви вирішили зробити консольний прототип без графічної оболонки для 
залучення інвесторів. 

Хоч проєкт і невеликий, дедлайни досить обмежені, тому вам варто подумати 
яким чином розділяти задачі в команді. Зазвичай в команді можуть 
бути такі ролі: 
- дизайнер (ака людина, яка займається графічним/консольним інтерфейсом,
   менюшкою і т.п.)
- core-розробник (ака людина, яка пише основний рушій гри)
- левел-дизайнер (людина, яка проектує рівні, використовуючи вже написані 
   інструменти)
- сценарист (придумує сюжет, прописує персонажів)
- game economy designer (людина, яка продумує якісь числові аспекти гри по 
   типу балансу, внутрішньоігрової економіки і т.п.)
- редактор (перевіряє і модерує текст/сюжет)

Звісно, в такому маленькому проєкті навряд буде яскраво виражена та чи інша 
роль, проте вам точно треба якимось чином розділяти задачі. 


__Зауваження__: так як створення сюжету і написання тексту є частиною 
розробки гри, це також буде оцінюватись. [Нинішній текст](./ukrainian_version.md) 
був згенерований за допомогою ChatGPT і перекладений на українську з 
невеликими ручними поправками. Звісно, ми хочемо гарний український дубляж, 
тому додатково наведена оригінальна [англійська версія](./english_version.md), 
яка написана більш кучеряво. За гарний переклад можна отримати додаткові бали 
(хоча я б не виділяв на це багато часу).

------------------
Для розробки гри вам знадобляться деякі команди з стандартної бібліотеки 
Python, зокрема бібліотека для роботи з випадковими величинами `random`:

```python
# імпортування бібліотеки 
import random 

# генерування випадкового цілого числа від 0 до 3
x = random.randint(0, 3)

# генерування випадкового (рівномірно розподіленого) дійсного числа
# від 0 до 1 
y = random.uniform(0, 1)

# випадковий вибір одного з наведених варіантів 'one', 'two' або 'three'
z = random.choice(['one', 'two', 'three'])
```

а також бібліотеки для роботи з таймером `time`:
```python

import time 

# повернути час як к-ть секунд від моменту Epoch (1 січня 1970)
t = time.time()

# засікти скільки часу в секундах зайняв шматок коду з попереднього
# присвоєння
print("elapsed time:", time.time() - t)
```

## Загальні механіки
Гравець починає гру зі створення персонажа. Якщо гравець 
помирає на будь-якому з рівнів, то гра закінчується. При цьому, в кінці 
має вивестися текст:

```
  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                
```

Такий текст варто зберігати у змінних, використовуючи потрійні лапки:

```python
game_over = """
  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                
"""

print(game_over)
```

Кожен раз, коли гра очікує введення від гравця, на екрані повинне 
з'являтись поле для введення.

``` 
>>>---> 
```

(___Зауваження___: гарною практикою буде присвоїти цей рядок якійсь змінній і потім
завжди її використовувати, бо раптом замовники скажуть, що `#->>>` виглядає
краще)

Взаємодію з користувачем варто зробити через нескінченний цикл та
ігнорувати всі некоректні введення з клавіатури. Приклад:

```python
while True: 
    print("Ви хочете вийти? (yes/no):")
    x = input(">>>---> ")
    if x == "yes":
        # тут відбувається вихід з циклу  
        break
    elif x == "no":
        # тут відбувається якась інша логіка
        pass 
    else: 
        # ігноруємо всі інші некоректні введення
        pass
```
Якщо гравець ввів некоректні дані, йому треба вивести повідомлення про це. 

В будь-який момент гравець може закінчити гру. Для цього йому необхідно ввести 
кодове слово `exit` і підтвердити це. Зробити це можна в будь-якому місці 
програми за допомогою вбудованої функції:

```python
x = input(">>>---> ")
if x == "exit": 
    if input("Ви бажаєте вийти? (yes/no)\n>>>---> ") == "yes": 
        exit(0)
```

## Початок
Гра має вивести [повідомлення](./ukrainian_version.md). 

## Cтворення персонажа
[Повідомлення](./ukrainian_version.md). 

Далі необхідно розподілити основні властивості персонажа: Сила, 
Спритність і Інтелект. На початку гри є 10 очків для розподілення. 
З кожним пройденим рівнем додається ще одне очко. Гравець сам 
вирішує куди йому розподілити їх. 

Приклад: 
- гравець згенерував персонажа і розподілив очки як 
    (3 Сила, 2 Спритність, 5 Інтелект). 
- гравець пройшов два рівні і розподілив додаткові два очки по одному 
    в Силу і Спритність. Таким чином, на 3 рівні гравець має показники
  (4 Сила, 3 Спритність, 5 Інтелект)


## Меню 

Меню має виводитись після закінчення кожного рівня. Тут Гравець може обрати: 
1. грати наступний рівень 
2. показати всю інформацію персонажа (рівень, ім'я, раса, вік, характеристики)
3. змінити ім'я
4. використати додаткові очки характеристик (які були зароблені після 
   проходження рівнів)
5. вийти 

## Рівень 1 (Вгадай число)

[Повідомлення](./ukrainian_version.md).

Як ви могли зрозуміти, на цьому рівні гравцю необхідно відгадати число від 
0 до 10. Якщо гравець не вгадує, __то магічна куля має сказати чи загадане число
більше чи менше__. Всього у гравця є 3 спроби, якщо всі 3 були неуспішними, 
то гравець закінчує гру. 

__Зауваження:__ передбачте можливість змінити к-ть допустимих спроб і рамки чисел. 

## Рівень 2 (Парадокс Монті Голла)

[Повідомлення](./ukrainian_version.md).

Гра має згенерувати 3-є дверей: одна дає можливість гравцеві виграти, інші 
дві ведуть до програшу. Після генерації гра має запитати у користувача 
вибір (1, 2 або 3). Коли користувач обере двері, скажімо 1, гра має 
серед інших двох дверей показати де знаходиться один програш. Після цього 
користувач має можливість змінити вибір. 

Якщо гравець виграв, то рухається далі. Програв -- гра закінчується.


## Рівень 3 (Кімната містичних рівнянь)

[Повідомлення](./ukrainian_version.md).

На цьому левелі гравець повинен вирішити 5 рівнянь з обмеженим часом. 
Базова к-ть часу на кожне рівняня -- 60 секунд. За кожен пункт свого 
інтелекту гравець отримує додатково ще 10 секунд. Якщо гравець не встиг 
відповідь до закінченого часу -- гра завершується. 

Рівняння мають бути згенеровані випадковим чином, проте 
збільшувати свою складність продовж левела. Віповідь має бути 
перевірена з **точністю до двох знаків після коми**: 

```python
real = 0.15
answer = 0.152
ERROR = 0.01

if abs(real - answer) < ERROR:
    print("GOOD")
```

Якщо квадратне рівняння має два розв'язки, то гравець має вводити БІЛЬШИЙ.

Рекомендується зробити такі рівняння:
1. лінійне рівняння ax = b з цілими коефіцієнтами 
2. лінійне рівняння ax = b з дійсними коефіцієнтами
3. квадратне рівняння з додатнім дискримінантом і цілими коефіцієнтами 
   ax^2 + bx + c = 0
4. квадратне рівняння з невід'ємним дискримінантом і більшими цілими 
   коефіцієнтами ax^2 + bx + c = 0 
5. квадратне рівняння з невід'ємним дискримінантом і дійсними цілими 
    коефіцієнтами ax^2 + bx + c = 0

__Зауваження__: для згенерованого рівняння умови мають бути виконані. Для 
цього можна вивести умову генерації або просто генерувати поки умова не буде 
виконана

```python
while True: 
    a, b, c = ...     # якась генерація
    
    # якщо умова виконується -- виходимо з циклу
    if discriminant(a, b, c) > 0: 
        break 
```

__Зауваження__: додатковим бонусом буде балансування цього рівня, тобто 
підбір такого часу і правил додавання часу за інтелект, щоб середньостатистичній 
людині було важко пройти левел, але можливо.

## Рівень 4 
## Рівень 5
## Рівень 6 
## Рівень 7 
## Рівень 8 
## Рівень 9 
## Рівень 10
