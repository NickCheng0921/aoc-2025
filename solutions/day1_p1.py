"""
Safe has dial with arrow on it
Dial turns CW and CCW

Solution document has sequence of rotations, one a line
L or R, L goes towards lower, R goes higher
pos 11, R8, pos 19

Actual password is # of times dial is left pointing at 0 after any rot in seq
"""

dial, point0 = 50, 0

with open("../input/day1.txt", "r") as f:
    rotation_list = [x for x in f.read().split() if x]

#  verify parsing
#print(rotation_list[:5], rotation_list[-5:])

for rotation in rotation_list:
    direction, amount = rotation[:1], int(rotation[1:])
    sign = 1 if direction == "R" else -1

    dial = (dial + sign*amount) % 100
    point0 += dial == 0

print(point0)