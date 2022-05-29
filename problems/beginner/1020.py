n = int(input())

#years
years = n // 365
n = n - years*365
#months
months = n // 30
n = n - months*30
#days
days = n

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))
