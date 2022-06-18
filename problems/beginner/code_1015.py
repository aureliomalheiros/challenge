"""
Problem 1015 with python
"""
import math
line1 = input("")
line2 = input("")

line_part1 = line1.split(" ")
line_part2 = line2.split(" ")

x1 = float(line_part1[0])
y1 = float(line_part1[1])

x2 = float(line_part2[0])
y2 = float(line_part2[1])

operation = math.sqrt((x2-x1)**2 + (y2-y1)**2)
result = f'{operation}'
print(result)
