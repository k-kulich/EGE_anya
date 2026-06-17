def ex1():
    """29979"""
    import math
    # файл A
    # все разделяет y = -1,25x + 25

    # списки-кластеры, куда мы будем распределять точки
    clasters_A = [[], []]  # оба кластера - это списки в списке файла
    # для B
    clasters_B = [[], [], []]
    
    # надо теперь открыть файл и все из него прочитать
    with open('data/27_A_29979.txt', mode='r') as infile:
        for line in infile:
            x, y = map(float, line.replace(',', '.').split())  # map - делает из строк float; 
            # split() делит line по пробелам на подстроки 
            # line = '6,203000 10,215302' -> split() -> ['6,203000', '10,215302'] -> map -> (6.203000, 10.215302)
            point = (x, y)  # делаем из них пару, чтобы было удобнее записывать в список
            # надо проверить, где лежит эта точка: выше или ниже прямой
            y_test = -1.25 * x + 25  # соответствующий y на прямой
            if y > y_test:  # пусть первый кластер - нижний, тогда тут надо класть во второй
                clasters_A[1].append(point)  # добавляем точку в кластер
            else:
                clasters_A[0].append(point)

    # y = x + 5 и x = 25
    with open('data/27_B_29979.txt', mode='r') as infile:
        for line in infile:
            x, y = map(float, line.replace(',', '.').split())
            y_test = x + 5
            point = (x, y)
            if y > y_test:  # попали в верхний кластер
                clasters_B[0].append(point)
            elif x > 25:  # попали в правй кластер
                clasters_B[2].append(point)
            else:
                clasters_B[1].append(point)

    # все, данные считали, а теперь надо найти числа по условию
    # А_1 - в кластере с наименьшим количеством точек число точек, абсцисса которых не больше 
    # абсциссы центра этого кластера
    # А_2 - расстояние между центрами кластеров
    centers_A = []  # сюда положим координаты центров соответствующих кластеров
    centers_B = []
    # как определить центры? центр - это точка, сумма расстояний до которой минимальна

    def center(claster):
        dist_sums = []  # суммы расстояний
        for p in claster:
            # ищем сумму расстояний для текущей точки
            summa = sum(math.dist(p, p1) for p1 in claster)
            dist_sums.append((summa, p))
        # в итоге нам нужна точка с минимальной суммой
        return min(dist_sums)[1]  # вернуть координаты точки с минимальной суммой
    
    for cl in clasters_A:
        centers_A.append(center(cl))  # по очереди добавляем центры кластеров

    for cl in clasters_B:
        centers_B.append(center(cl))  # кидаем центры B    
    
    # определим кластер с минимальным числом точек
    mn_idx = 0 if len(clasters_A[0]) <= len(clasters_A[1]) else 1
    a_1 = 0  # сюда будем считать точки
    for x, y in clasters_A[mn_idx]:
        cx, cy = centers_A[mn_idx]  # координаты центра этого кластера
        if x <= cx:  # если абсцисса не больше, то условие выполняется
            a_1 += 1
    a_2 = math.dist(centers_A[0], centers_A[1])  # и так найдем расстояние между центрами
    print(a_1, int(a_2 * 10_000))  # надо в ответ a_2 на 10k
    # ответ на A: 141 129966

    b_1 = 0
    # теперь надо для B
    mn_idx = clasters_B.index(min(clasters_B, key=len))  # ищем минимальный по кол-ву точек автоматически
    mx_idx = clasters_B.index(max(clasters_B, key=len))
    mid = 3 - mn_idx - mx_idx  # index оставшегося кластера
    # B_1 - число точек, находящихся внутри квадрата с центром в центре этого же кластера, 
    # сторонами, параллельными координатным осям и длиной 2,0
    cx, cy = centers_B[mid]
    for x, y in clasters_B[mid]:
        # проверим, что внутри квадрата: разность координат (любых 2) меньше 1
        if abs(x - cx) < 1 and abs(y - cy) < 1:
            b_1 += 1
    # B_2 - расстояние по оси ординат между центрами кластеров с наименьшим и наибольшим
    # количеством точек
    b_2 = abs(centers_B[mn_idx][1] - centers_B[mx_idx][1])
    print(b_1, int(b_2 * 10_000))
    # 132 127070


def task1():
    # 28946
    import math
    clasters_A = [[], []]  
    clasters_B = [[], [], []]
    
    with open('data/27_A_29979.txt', mode='r') as infile:
        for line in infile:
            coords = line.replace(',', '.').split()
            x, y = float(coords[0]), float(coords[1])
    
    # IndexError - где-то неверно берется индекс; возможно, он слишком большой/маленький
    # (в списке или строке нет такого числа элементов)
    # TypeError - что-то намудрили с типами данных: смотрим (если есть float), везде ли у нас
    # цифры разделяются точками; смотрим, каких типов данных у нас объекты (например, пытаемся
    # изменить элемент строки -> надо ее превратить сначала в список с помощью list())
    # ZeDivisionError - ошибка деления на 0 (думаем, как такое могло получится)     
