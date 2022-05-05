from itertools import combinations_with_replacement

word, num = input().split()
cwrs = combinations_with_replacement(sorted(word), int(num))

for cwr in cwrs:
    print("".join(cwr))
