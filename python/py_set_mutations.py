n = int(input())
set_a = set(map(int, input().split()))

num = int(input())
for _ in range(num):
    cmd, m = input().split()
    set_b = set(map(int, input().split()))

    # getattr(set_a, cmd)(set_b)
    if cmd == "update":
        set_a.update(set_b)
    elif cmd == "intersection_update":
        set_a.intersection_update(set_b)
    elif cmd == "difference_update":
        set_a.difference_update(set_b)
    elif cmd == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)

print(sum(set_a))
