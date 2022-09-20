from collections import defaultdict

size_a, size_b = map(int, input().split(" "))
group_a = defaultdict(list)

for index in range(1, size_a+1):
    word = input()
    group_a[word].append(index)

for _ in range(size_b):
    word = input()
    if word in group_a.keys():
        print(*group_a[word])
    else:
        print(-1)
