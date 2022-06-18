"""
Problem 1019 with python
"""
value = int(input())

hours = value//3600
minutes = (value - (hours*3600))//60
seconds = (value%60)
result = f'{hours}:{minutes}:{seconds}'
print(result)
