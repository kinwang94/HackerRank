from collections import Counter

number_shoes = input()
size_list = Counter(map(int, input().split(" ")))
number_customer = int(input())

revenue = 0
for _ in range(number_customer):
    size, price = map(int, input().split(" "))
    if size_list[size] > 0:
        revenue += price
        size_list[size] -= 1

print(revenue)
