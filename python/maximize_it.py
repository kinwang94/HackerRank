from itertools import product

num, mod = list(map(int, input().split()))
digital_list = [list(map(int, input().split()[1:])) for _ in range(num)]

combs = list(product(*digital_list))
value_list = [sum(list(map(lambda x: x ** 2, comb))) % mod for comb in combs]

print(max(value_list))
