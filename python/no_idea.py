happiness = 0

n, m = list(map(int, input().split()))
num_list = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

for num in num_list:
    if num in set_a:
        happiness += 1
    elif num in set_b:
        happiness -= 1

print(happiness)
# print(sum([(num in set_a) - (num in set_b) for num in num_list]))
