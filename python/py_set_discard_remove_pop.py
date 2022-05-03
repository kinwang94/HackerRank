n = int(input())
s = set(map(int, input().split()))

m = int(input())
for _ in range(m):
    cmd, *attr = input().split()

    if cmd == "pop":
        s.pop()
    elif cmd == "discard":
        s.discard(int(*attr))
    elif cmd == "remove":
        s.remove(int(*attr))

print(sum(s))
