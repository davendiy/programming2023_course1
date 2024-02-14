import math 

n = int(input()) 
res = sum(math.log10(k) for k in range(1, n+1))
print(math.ceil(res) if res else 1)
