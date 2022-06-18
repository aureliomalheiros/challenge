"""
Problem 1020 with python
"""
n = int(input())

#years
years = n // 365
n = n - years*365
#months
months = n // 30
n = n - months*30
#days
days = n

print(f'{years} ano(s)')
print('{months} mes(es)')
print('{days} dia(s)')
