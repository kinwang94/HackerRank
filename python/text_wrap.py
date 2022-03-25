def wrap(string, max_width):
    return "\n".join([string[index:(index + max_width)] for index in range(0, len(string), max_width)])
