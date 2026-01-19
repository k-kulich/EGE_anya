def from_base_to_decimal(number, base, x):
    result = 0
    for i in range(len(number)):
        if number[i] == 'x':
            result += x * (base ** (len(number) - i - 1))
        else:
            result += int(number[i]) * (base ** (len(number) - i - 1))
    return result

res_min = 10 ** 9
min_x = 10 ** 9
base = 17
number1 = '11x586' 
number2 = '5x211'
for x in range(base):
    num1 = from_base_to_decimal(number1, base, x)
    num2 = from_base_to_decimal(number2, base, x)
    e = num1 + num2
    if (e % 49 == 0) and x < min_x:
        min_x = x
        res_min = e
print( "x:", min_x)
print("e:", res_min // 49)

