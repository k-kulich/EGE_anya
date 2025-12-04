import itertools  # встроенный модуль, который содержит комбинаторные штуки

def task2():
    # (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
    # содержащий все наборы аргументов, при которых функция F ложна
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    pass  # ничего не делать

    for x, y, z, w in itertools.product((0, 1), repeat=4):
        F = (x and not y) or (y == z) or not w
        if F == 0:
            print(x, y, z, w, int(F))


def task1():
    # ¬(¬(x→¬w)∧z)∧¬(w→z)∧(x→¬z)
    #   ?   ?   ?   ?   F
    #   1	0	 	0	1
    #   1	0	 	 	0
    #   	1	   	1	0

    # →  == <=   следование можно заменить на <=
    # x→¬w    мы можем записать как     x <= (not w)

    #   x   w   x→w     x <= w
    #   0   0   1       1
    #   0   1   1       1
    #   1   0   0       0
    #   1   1   1       1

    # print("x y z w | F")
    # for x, y, z, w in itertools.product((0, 1), repeat=4):
    #     F = not (not (x <= (not w)) and z) and not (w <= z) and (x <= (not z))
    #     print(x, y, z, w, '|', int(F))

    #             0    1    2    3
    var_names = ["x", "y", "z", "w"]

    result = 0  # здесь будем считать кол-во подходящих перестановок

    for perm in itertools.permutations((0, 1, 2, 3)):  # эта функция генерирует все перестановки переданного объекта
        # строки для красоты, не для смысла
        print("Текущая перестановка: ", perm)
        for i in perm:
            print(var_names[i], end=' ')
        print("-- текущая перестановка")

        # смысл продолжается отсюда
        can_be_first = can_be_second = can_be_third = 0  # будем хранить кол-ва строк, которые могут быть 1, 2 или 3
        for x, y, z, w in itertools.product((0, 1), repeat=4):  # здесь мы перебираем значения
            F = not (not (x <= (not w)) and z) and not (w <= z) and (x <= (not z))
            #            0  1  2  3
            variables = [x, y, z, w]  # текущая строка в порядке    x - y - z - w
            
            # row чтобы понять, где сейчас стоит какая переменная
            row = []  # будет обозначать ряд в текущей расстановке (как оно выглядит в таблице)
            for i in perm:  # здесь перебираем расстановку: смотрим, какая переменная в каком стобце сейчас стоит
                row.append(variables[i])  # записываем порядок, в котором стоят переменные (y - x - w - z, например)
            print(row)

            if F == 1 and row[0] == 1 and row[1] == row[3] == 0:
                can_be_first += 1
            if F == 0 and row[0] == 1 and row[1] == 0:
                can_be_second += 1
            if F == 0 and row[1] == row[3] == 1:
                can_be_third += 1
        
        
        if can_be_first > 0 and can_be_second > 0 and can_be_third > 0:
            print(">>> Перестановка", perm, "подходит!!!")
            result += 1

    print("\nВсего подходит перестановок: ", result)            


task1()
