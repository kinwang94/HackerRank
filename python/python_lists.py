if __name__ == '__main__':
    N = int(input())

    container = []
    for _ in range(N):
        args = input().split(" ")
        command = args[0]
        if command == "insert":
            container.insert(int(args[1]), int(args[2]))
        elif command == "print":
            print(container)
        elif command == "remove":
            container.remove(int(args[1]))
        elif command == "append":
            container.append(int(args[1]))
        elif command == "sort":
            container.sort()
        elif command == "pop":
            container.pop()
        elif command == "reverse":
            container.reverse()
