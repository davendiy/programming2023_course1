import math

a, b, c, d, f = [float(d) for d in input().split()]
half_perim = (a + b + f) / 2
half_perim_2 = (c + d + f) / 2

geron_1 = math.sqrt(half_perim * (half_perim - a) * (half_perim - b) * (half_perim - f))
geron_2 = math.sqrt(half_perim_2 * (half_perim_2 - c) * (half_perim_2 - d) * (half_perim_2 - f))
area = geron_1 + geron_2
print(f"{area:.4f}")
