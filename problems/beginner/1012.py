line = input("")
line_part = line.split(" ")

a = float(line_part[0])
b = float(line_part[1])
c = float(line_part[2])

pi = 3.14159

Atriangle = (a*c)/2
Acircle = pi*c**2
Atrapeziun = ((a+b)*c)/2
Asquare = b*b
Arectangle = a*b

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (Atriangle, Acircle, Atrapeziun, Asquare, Arectangle))

"""
Presentation error!!!!!
print("TRIANGULO: {: .3f}" .format(Atriangle))
print("CIRCULO: {: .3f}" .format(Acircle))
print("TRAPEZIO: {: .3f}" .format(Atrapeziun))
print("QUADRADO: {: .3f}" .format(Asquare))
print("RETANGULO: {: .3f}" .format(Arectangle))
"""

