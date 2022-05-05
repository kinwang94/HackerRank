from itertools import permutations

word, num = input().split()
perms = permutations(sorted(word), int(num))

for perm in perms:
    print("".join(perm))
