from collections import OrderedDict

number = int(input())
word_dict = OrderedDict()

for _ in range(number):
    word = input()
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(len(word_dict))
print(*word_dict.values())
