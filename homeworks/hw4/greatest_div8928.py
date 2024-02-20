
n = int(input())
sqrt_n = int(n ** 0.5)

res_n = 1 
min_div = 1 

i = 2

while res_n != n and i < sqrt_n: 
    
    for prob_i in [i, sqrt_n - i + 2]:
        prob_i_orig = prob_i
        while n % prob_i == 0: prob_i *= prob_i_orig

        if n % prob_i == 0: 
            res_n *= prob_i 
            min_div = min(min_div, prob_i_orig)
            min_div = min(min_div, n // prob_i)
    i += 1


print(n // min_div)
