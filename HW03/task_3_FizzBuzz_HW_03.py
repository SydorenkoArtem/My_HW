# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

txt = open('task_2_fizzbuzz_hw03.txt', 'r')  # в файле теперь file descriptor
txt_for_write = open('task_3_fizzbuzz_hw03.txt', 'w')

for line in txt:  # для каждой строки в файле
    list = line.split()  # строку из файла формируем в список
    fizz = int(list[0])
    buzz = int(list[1])
    number = int(list[2])

    for i in range(1, number + 1):
        if i % fizz == 0 and i % buzz == 0:
            txt_for_write.write('FB')
            txt_for_write.write(' ')
        elif i % fizz == 0:
            txt_for_write.write('F')
            txt_for_write.write(' ')
        elif i % buzz == 0:
            txt_for_write.write('B')
            txt_for_write.write(' ')
        else:
            txt_for_write.write(str(i))
            txt_for_write.write(' ')
            i += 1
    txt_for_write.write('\n')
txt.close()  # закрытие файла
txt_for_write.close()  # закрытие файла для записи
