# (69 < y +2x) ∨(A > x)∨ (A > y)

# организуем перебор 3мя циклами
for a in range(10000):  # с запасом
    is_a_correct = True  # подходит ли это значение как ответ?
    for y in range(1000):
        for x in range(1000):
            if ((69 < y + 2 * x) or (a > x) or (a > y)) == False:  # если ложно, то обкакался
                is_a_correct = False  # обосрались
                break
        if not is_a_correct:  # если уже обкакались, дальше перебирать не надо
            break
    # в ответ записываем первое А, при котором не обкакался
    if is_a_correct:  # если до этого не прервался перебор, то не обосрались
        print(a)  # ответ 24
        break


# Для какого наименьшего целого неотрицательного числа A выражение
# (x^2 − 3x+ 2 > 0) ∨ (y > x^2 + 7) ∨ (xy < A)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x, y?

# 5437

for a in range(1, 1000):
    is_a_correct = True
    for z in range(1000):
        for y in range(1000):
            for x in range(1000):
                # print(z, y, x, a)
                if (((z % 115 != 0) and (y % 78 != 0) and (x % 51 != 0)) or (x % a == 0)) == False:
                    is_a_correct = False
                    break
            if not is_a_correct:
                break
        if not is_a_correct:
            break
    if is_a_correct: 
        print(a)  # 1
