k = int(input())
room_number_list = list(map(int, input().split()))

single = set()
multiple = set()
for number in room_number_list:
    if number in single:
        multiple.add(number)
    else:
        single.add(number)

captain_room = single.difference(multiple)
print(captain_room.pop())
