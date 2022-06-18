"""
Problem 1035 with python
"""
line = input("")
line_break = line.split(" ")

A = int(line_break[0])
B = int(line_break[1])
C = int(line_break[2])
D = int(line_break[3])

bool_operation = (B > C and D > A) and (C+D) > (A + B) and C > 0 and B > 0 and (A % 2) == 0

if bool_operation:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    