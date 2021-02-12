students = {'Иванов Иван': [6, 5, 9],
            'Петров Петр': [5, 8, 8, 10],
            'Андреев Андрей': [9, 8, 10],
            'Борисов Борис': [6, 5, 3],
            'Суровый Эдуард': [4, 6, 8, 5],
            'Забытый Иван': [4, 5, 4, 7, 5]}
dictionary = {}

for surname, numbers in students.items():
    numbers = sum(numbers) / len(numbers)
    new_dict = dictionary.update(dict.fromkeys([surname], numbers))

max_number = max(dictionary.values())
min_number = min(dictionary.values())

for surname, value in dictionary.items():
    if value == max_number:
        print(surname, value)
    elif value == min_number:
        print(surname, value)
