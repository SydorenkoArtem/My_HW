def low_letters(string):
    string = string.lower()
    return string


def upper_letters(string):
    string = string.upper()
    return string


string_1 = str(input('Введите строку:\n'))

print(low_letters(string_1))
print(upper_letters(string_1))


# C помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!
list_1 = ['marShMalLow', 'STrAWbeRRy', 'POtaTo', 'ORangE']
list_2 = ['pizza', 'bread', 'cup', 'tea', 'lemon']
function_1 = list(map(low_letters, list_1))
function_2 = list(map(upper_letters, list_2))

print(function_1)
print(function_2)
