from collections import deque

case = int(input())
for _ in range(case):
    size = input()
    queue = deque(map(int, input().split()))

    for cube in sorted(queue, reverse=True):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")
