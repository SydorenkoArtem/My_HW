def low_letters(string):
    string = string.lower()
    return string


def list_text(words):
    new_list_1 = []

    for line in txt:
        new_line = "".join(c for c in line if c not in ('!', '.', ':', ';', ',', '?'))
        list_words = new_line.split()
        new_list_1 += list_words

    return new_list_1


def dict_frequency():
    dictionary = {}
    right_list = list_text(txt)
    new_list = list(map(low_letters, right_list))

    for i in new_list:
        counter = new_list.count(i)
        new_dict = dictionary.update(dict.fromkeys([i], counter))
    print(dictionary)


txt = open('english_text.txt', 'r')

dict_frequency()
