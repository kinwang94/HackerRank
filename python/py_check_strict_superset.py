status = True

set_a = set(map(int, input().split()))
sets = int(input())

for _ in range(sets):
    set_test = set(map(int, input().split()))
    if not set_a.issuperset(set_test):
        status = False

print(status)
