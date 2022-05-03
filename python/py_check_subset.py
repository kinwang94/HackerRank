times = int(input())

for _ in range(times):
    length_a = int(input())
    set_a = set(map(int, input().split()))
    length_b = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))

