line = 100 * '3' + 55 * '1' + 1000 * '0'
while '10' in line or '11' in line or '330' in line:
    if '10' in line:
        line = line.replace('10', '1', 1)
    elif '11' in line:
        line = line.replace('11', '3', 1)
    elif '330' in line:
        line = line.replace('330', '100', 1)
counter = 0
for sym in line:
    if sym.isdigit() and int(sym) % 2 != 0:
        counter = counter + int(sym)
print(counter)
