from collections import Counter

string = sorted(input())
common = Counter(string).most_common(3)

for character in common:
    print(*character)
