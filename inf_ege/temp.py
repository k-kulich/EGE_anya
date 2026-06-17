import csv
from random import randint, choice

def create_data():
    schools = [f'Школа № {randint(150, 750)}' for _ in range(10)]

    min_sum = 300
    count = 0
    sc_count = dict.fromkeys(schools, 0)
    with open('temp.csv', mode='w', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=';')
        for line in [(choice(schools), randint(1, 100), randint(1, 100), randint(1, 100)) for _ in range(1000)]:
            writer.writerow([line[0], str(line[1]), str(line[2]), str(line[3])])
            m, r, i = line[1:]
            if m > 50 or i > 50:
                min_sum = min(min_sum, sum(line[1:]))
            if r < 60:
                count += 1
            sc_count[line[0]] += 1

    print(f'fillind completed.\n\nAnswers:\ntask 1:\t\t{min_sum}\ntask 2:\t\t{count}')
    for school in schools:
        print(school, sc_count[school])


create_data()

"""
Answers:
task 1:         67
task 2:         597
Школа № 223 113
Школа № 363 101
Школа № 601 92
Школа № 170 101
Школа № 318 103
Школа № 473 100
Школа № 576 98
Школа № 555 106
Школа № 604 77
Школа № 615 109
"""
