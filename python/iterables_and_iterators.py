from itertools import combinations

_ = int(input())
letter = input().split()
num = int(input())

combs = list(combinations(letter, num))
contain = [comb for comb in combs if "a" in comb]

print(f"{len(contain) / len(combs):.3f}")
