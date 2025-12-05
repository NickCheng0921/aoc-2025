"""
Given grid of @ and . symbols
Find @ positions with < 4 @s in their adjacent 8

You can remove them

Find how many we can remove

Easier to work w/ char array than string here

Brutius force
"""

with open("../input/day4.txt", "r") as f:
    input_text = f.read()

arr = [list(x) for x in input_text.split() if x]

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

while(True):
    removed = 0
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == "@":
                if check_accessible(arr, r, c, rows, cols):
                    removed += 1
                    arr[r][c] = "."
    
    accessible += removed
    if not removed:
        break

print(accessible)

