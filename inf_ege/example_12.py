# здесь исполнитель работает именно со строкой - массив символов

def task1():
    line = "8" * 68  # так мы получим строку из 68 цифр 8
    while '222' in line or '888' in line:  #  ПОКА нашлось (222) ИЛИ нашлось (888)
        if '222' in line:  # ЕСЛИ нашлось (222)
            line = line.replace('222', '8', 1)  # ТО заменить (222, 8)
        else:  # ИНАЧЕ заменить (888, 2)
            line = line.replace('888', '2', 1)
    print(line)
    
    result = 0  # сюда запишем сумму всех цифр в строке
    for sym in line:  # перебираем все символы строки
        if sym.isdigit():  # если это цифра
            result = result + int(sym)   # то переведем ее в тип int и прибавим к сумме
    print(result)
    

def task2():
    line = '>' + '1' * 10 + '2' * 20 + '3' * 30
    while ('>1' in line) or ('>2' in line) or ('>3' in line):
        if '>1' in line:
            line = line.replace('>1', '22>', 1)
        if '>2' in line:
            line = line.replace('>2', '2>', 1)
        if '>3' in line:
            line = line.replace('>3', '1>', 1)
    
    result = 0  # сюда запишем сумму всех цифр в строке
    for sym in line:  # перебираем все символы строки
        if sym.isdigit():  # если это цифра
            result = result + int(sym)   # то переведем ее в тип int и прибавим к сумме
    print(result)


task2()
