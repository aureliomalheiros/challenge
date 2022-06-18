"""
Problem 1012 with Python
"""
line = input("")
line_part = line.split(" ")

a = float(line_part[0])
b = float(line_part[1])
c = float(line_part[2])

PI = 3.14159

Atriangle = (a*c)/2
Acircle = PI*c**2
Atrapeziun = ((a+b)*c)/2
Asquare = b*b
Arectangle = a*b

RESULT_1 = f'TRIANGULO: {Atriangle}\nCIRCULO: {Acircle}\n'
RESULT_2 = f'TRAPEZIO: {Atrapeziun}\nQUADRADO: {Asquare}\nRETANGULO: {Arectangle}'

print(RESULT_1+RESULT_2)
