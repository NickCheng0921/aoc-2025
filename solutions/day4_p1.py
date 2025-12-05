"""
Given grid of @ and . symbols
Find @ positions with < 4 @s in their adjacent 8

123
456
789

Return number of accessible @s

0, 7
..@@.@@x@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

with open("../input/day4.txt", "r") as f:
    input_text = f.read()

arr = [x for x in input_text.split() if x]

rows, cols = len(arr), len(arr[0])
accessible = 0

def check_accessible(grid, x, y, rows, cols):
    iters = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    nearby = 0
    for dx, dy in iters:
        px = x+dx
        py = y+dy
        #print(dx, dy, "  ", px, py)
        if px >= 0 and px < rows and py >= 0 and py < cols:
            #print(f"    {grid[px][py]} at {px} {py}")
            nearby += grid[px][py] == "@"
    return nearby < 4


import numpy as np
newg = np.zeros((rows, cols))

for r in range(rows):
    for c in range(cols):
        if arr[r][c] == "@":
            accessible += check_accessible(arr, r, c, rows, cols)
            newg[r][c] = 1

print(accessible)