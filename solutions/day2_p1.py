"""
Input has produc tID ranges
Each range is separated by commas

find invalid IDs by looking for ID making of some sequence of digits repeated twice

17443749659 too low
18595663837 too low
21843161750 too high

Brute force
"""
import math

with open("../input/day2.txt", "r") as f:
    ranges_file = f.read().split()[0]

ranges = ranges_file.split(",")

def return_invalids(rangee):
    found = set({})
    start, end = rangee.split("-")
    #print(rangee, start, end)
    for i in range(int(start), int(end)+1):
        if len(str(i)) % 2 == 1:
            continue
        pal=True
        str_num = str(i)
        for j in range( int(len(str_num)/2) ):
            if str_num[j] != str_num[math.ceil(len(str_num)/2)+j]:
                pal=False
                break
        if pal:
            #print(i)
            found.add(i)
    return found

sum_ct = 0

found_set = set({})
for rang in ranges:
    found = return_invalids(rang)

    for item in found:
        found_set.add(item)


for item in found_set:
    sum_ct += item

print(sum_ct)