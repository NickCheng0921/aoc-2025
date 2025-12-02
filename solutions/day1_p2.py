"""
Safe has dial with arrow on it
Dial turns CW and CCW

Solution document has sequence of rotations, one a line
L or R, L goes towards lower, R goes higher
pos 11, R8, pos 19

Actual password is # of times dial clicks past 0 while following list

5660, 6156, 5748 too high
"""

dial, click0 = 50, 0

with open("../input/day1.txt", "r") as f:
    rotation_list = [x for x in f.read().split() if x]

#  verify parsing
#print(rotation_list[:5], rotation_list[-5:])

for rotation in rotation_list:
    direction, amount = rotation[:1], int(rotation[1:])
    sign = 1 if direction == "R" else -1

    intermed_dial = dial + sign * amount

    if sign > 0:
        # number of times we wrapped going right
        click0 += intermed_dial // 100
    else:
        # number of times we wrapped going left
        if intermed_dial <= 0:
            click0 += 1 + (-intermed_dial) // 100

    if intermed_dial < 0:
        intermed_dial = 100 - ((-intermed_dial)%100)
    dial = intermed_dial % 100

print(click0, dial)