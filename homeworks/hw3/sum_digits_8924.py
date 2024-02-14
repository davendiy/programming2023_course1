


n = input() 
amount = len([k for k in n if int(k) % 2 == 0])
res = sum(int(k) for k in n if int(k) % 2 == 0)
if amount: 
    print(res) 
else: 
    print(-1)
