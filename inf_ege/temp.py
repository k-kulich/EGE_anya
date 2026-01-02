for m in range(8):
    for n in range(100):
        line = '*' + m * '7' + 7 * '8' + n * '7'
        print(line)
        while '*7' in line or '*8' in line:
            if '*78' in line:
                line = line.replace('*78', '4*', 1)
            elif '*7' in line:
                line = line.replace('*7', '0*', 1)
            if '*8' in line:
                line = line.replace('*8', '8*', 1)
        print(line)
        summ = 0
        for sym in line:
            if sym.isdigit():
                summ += int(sym)
        if summ == 40:
            print(n + m )