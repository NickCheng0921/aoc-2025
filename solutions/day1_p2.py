"""
Safe has dial with arrow on it
Dial turns CW and CCW

Solution document has sequence of rotations, one a line
L or R, L goes towards lower, R goes higher
pos 11, R8, pos 19

Actual password is # of times dial clicks past 0 while following list

5660, 6156, 5748 too high
5657 right
"""

dial, click0 = 50, 0

with open("../input/day1.txt", "r") as f:
    rotation_list = [x for x in f.read().split() if x]

#  verify parsing
#print(rotation_list[:5], rotation_list[-5:])

# click it

# click0 = 0
# for rotation in rotation_list:
#     direction, amount = rotation[:1], int(rotation[1:])

#     if direction == "R":
#         for click in range(amount):
#             dial += 1
#             click0 += (dial % 100) == 0
#         dial = dial%100
#     else:
#         for click in range(amount):
#             dial -= 1
#             click0 += (abs(dial)%100) == 0
#         dial = dial%100

# print(click0)


for rotation in rotation_list:
    direction, amount = rotation[:1], int(rotation[1:])
    sign = 1 if direction == "R" else -1

    if sign > 0:
        click0 += (dial + sign*amount) // 100
    else:
        click0 += -(dial == 0) + ((100 - dial) + amount) // 100
    
    dial = (dial + sign*amount) % 100

print(click0)