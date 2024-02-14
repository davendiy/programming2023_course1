s = input()
fixed_s = ''
for el in s: 
    if el.isalnum() or el == ' ': 
         fixed_s += el.lower()

words = [el for el in fixed_s.split() if el == el[::-1]]
if not words: 
    print(0)
else: 
    max_len = 0 
    max_index = -1 
    for i, el in enumerate(words): 
         if len(el) > max_len: 
             max_len = len(el) 
             max_index = i
    print(max_index + 1)
