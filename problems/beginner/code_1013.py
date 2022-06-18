"""
Problem 1013 with python
"""
line  = input("")
line_part = line.split(" ")

a = int(line_part[0])
b = int(line_part[1])
c = int(line_part[2])

max_AB = (a + b + abs(a - b))/2
max_result = (max_AB + c + abs(max_AB - c))/2
RESULT = f'{max_result} eh maior'
print(RESULT)
