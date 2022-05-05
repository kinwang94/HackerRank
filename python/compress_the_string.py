from itertools import groupby

num_string = input()

print(*[(len(list(count)), int(key)) for key, count in groupby(num_string)])
