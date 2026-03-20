def to_other_base(number, base):
    result = ' '
    while number > 0:
        digit = number % base
        if digit < 10:
            result = result + str(digit)
        else:
            result = result + chr(ord('A') + digit - 10)
        number //=  base
    return result


y = 5 ** 50 + 25 ** 3 - 125
es = to_other_base(y, 5)
counter = 0
for sym in es:
    if sym == '4':
        counter = counter + 1
print(counter)
    
