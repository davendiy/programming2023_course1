

n = int(input())

start = 2
end = 2000

while True: 
    if end == start or end == start + 1: 
        print(start)
        break

    mid = (end + start) // 2
    if n % mid == 0 and n % (mid - 1) == 0: 
        start = mid
    else: 
        end = mid

