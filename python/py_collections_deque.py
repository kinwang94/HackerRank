from collections import deque

number = int(input())
queue = deque()

for _ in range(number):
    cmd, *value = input().split()

    # if value:
    #     getattr(queue, cmd)(*value)
    # else:
    #     getattr(queue, cmd)()

    if cmd == "append":
        queue.append(*value)
    elif cmd == "appendleft":
        queue.appendleft(*value)
    elif cmd == "pop":
        queue.pop()
    elif cmd == "popleft":
        queue.popleft()

print(*queue)
