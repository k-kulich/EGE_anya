line = '*' + 100 * '2' + 10 * '5' + 60 * '9'
while '*2' in line or '*5' in line or '*9' in line:
    if '*2' in line:
        line = line.replace('*2', '*', 1)
    elif '*5' in line:
        line = line.replace('*5', '6*', 1)
    elif '*9' in line:
        line = line.replace('*9', '7*', 1)
print(line)
