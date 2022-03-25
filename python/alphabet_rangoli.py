def print_rangoli(size):
    alphabet_list = list(map(chr, range(97, 123)))

    width = (4 * size) - 3
    col = list()
    for index in range(size):
        alpha = "-".join(alphabet_list[index:size])
        col.append((alpha[::-1] + alpha[1:]).center(width, "-"))

    print("\n".join(col[:0:-1] + col))
