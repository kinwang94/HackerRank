from itertools import combinations

word, num = input().split()
word = sorted(word)
num = int(num)

for n in range(1, num + 1):
    combs = combinations(word, n)
    for comb in combs:
        print("".join(comb))
