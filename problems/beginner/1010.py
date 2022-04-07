line1 = input("")
line2 = input("")

line_part1 = line1.split(" ")
line_part2 = line2.split(" ")

a = int(line_part1[0])
b = int(line_part1[1])
c = float(line_part1[2])

d = int(line_part2[0])
e = int(line_part2[1])
f = float(line_part2[2])

result = b*c + e*f

print("VALOR A PAGAR: R$ {:.2f}" .format(result))

