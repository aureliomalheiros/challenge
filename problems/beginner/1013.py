#from math import abs
import math
line  = input("")
line_part = line.split(" ")

a = int(line_part[0])
b = int(line_part[1])
c = int(line_part[2])

max_AB = (a + b + abs(a - b))/2
max_result = (max_AB + c + abs(max_AB - c))/2

print("%d eh o maior" %max_result)