def print_formatted(number):
    width = len(f"{number:b}")
    # width = number.bit_length()

    for num in range(1, number + 1):
        print(f"{num:>{width}d} {num:>{width}o} {num:>{width}X} {num:>{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)