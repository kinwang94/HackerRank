from collections import OrderedDict

number_item = int(input())
item_dict = OrderedDict()

for _ in range(number_item):
    *item_name, net_price = input().split()
    item_name = " ".join(item_name)
    net_price = int(net_price)

    if item_name not in item_dict.keys():
        item_dict[item_name] = net_price
    else:
        item_dict[item_name] += net_price

for item in item_dict.items():
    print(*item)
