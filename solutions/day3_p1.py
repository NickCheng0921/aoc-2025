"""
Batteries have value from 1-9
Arranged into banks
Each line is a single bank
In each bank, turn on two batteries
Joltage bank produces is equal to the number formed by the digits on the batteries turned on

Bank 12345 gives joltage 24 if 2 and 4 on
Find largest joltage each bank can make
Total is sum of joltage per bank

17149 too high

I dedicate my solution inspiration to labubu
Thought back to trapping rainwater, I was like, wait I need to find two towers
Ok, I can find one by doing max
Hmm, I can't max again cause the first tower is there...
I can pop it
Ok, I just call max again, figure out edge cases for L and R array and we done
"""

"""
Find largest 2 digit number we can form per line
We can max the array, then remove it w/ the index
Max again and keep track of index of this and last max, find biggest num we can make w/ these 3
"""


with open("../input/day3.txt", "r") as f:
    joltages = [x for x in f.read().split() if x]

jolt_sum = 0

def find_remove_max(lst):
    return max(lst), lst.index(max(lst))

for joltage_str in joltages:
    #print(joltage_str)

    X, pop_dat = find_remove_max(joltage_str)

    left = joltage_str[:pop_dat]
    right = joltage_str[pop_dat+1:]

    if not right:
        Y, _ = find_remove_max(left)
        #print(Y, X)
        jolt_sum += int(Y+X)
    elif not left:
        Y, _ = find_remove_max(right)
        #print(X, Y)
        jolt_sum += int(X+Y)
    else:
        Y1, _ = find_remove_max(left)
        Y2, _ = find_remove_max(right)
    
        #print((Y1, X), (X, Y2))
        jolt_sum += max(int(Y1+X), int(X+Y2))

print(jolt_sum)