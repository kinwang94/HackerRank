length_a = int(input())
set_a = set(map(int, input().split()))

length_b = int(input())
set_b = set(map(int, input().split()))

diff_list = list(set_a.difference(set_b)) + list(set_b.difference(set_a))
for diff in sorted(diff_list):
    print(diff)

# print(*sorted(diff_list), sep="\n")
