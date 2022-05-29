value = int(input())

hours = value//3600
minutes = (value - (hours*3600))//60
seconds = (value%60)

print("{}:{}:{}" .format(hours, minutes, seconds))