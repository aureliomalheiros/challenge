import math
line1 = input("")
line2 = input("")

line_part1 = line1.split(" ")
line_part2 = line2.split(" ")

x1 = float(line_part1[0])
y1 = float(line_part1[1])

x2 = float(line_part2[0])
y2 = float(line_part2[1])

result = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("%0.4f" %result)
