stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
idx = stdform.find('x')
base = str(float(stdform[0:idx]))
idx = stdform.find('^')
power = stdform[idx+1:]
print("This number in E notation is " + base + 'E' + power + '.')
# Type your code below
