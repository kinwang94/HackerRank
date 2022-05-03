import math

AB = int(input())
BC = int(input())

hyp = math.hypot(AB, BC)
angle = round(math.degrees(math.acos(BC / hyp)))
degree_sym = chr(176)

print(f"{angle}{degree_sym}")
