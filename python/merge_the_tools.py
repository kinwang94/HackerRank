def merge_the_tools(string, k):
    for index in range(0, len(string), k):
        slice_string = string[index:index+k]

        merge_string = []
        for char in slice_string:
            if char not in merge_string:
                merge_string.append(char)

        print("".join(merge_string))
