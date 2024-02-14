

m = input()
num = len(m)
cur_dec = pow(10, num)

m = int(m) 

while True: 
    if m < cur_dec: 
        cur_dec //= 10 
    
    if ((m ** 2) % (cur_dec * 10)) == m: 
        print(m) 
        break
    m -= 1 

