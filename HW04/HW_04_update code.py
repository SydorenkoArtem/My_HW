# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

txt = open('task_2_fizzbuzz_hw03.txt', 'r')
txt_w = open('task_3_fizzbuzz_hw03.txt', 'w')

for line in txt:
    fizz, buzz, number = map(int, line.split())

    for i in range(1, number + 1):
        if not i % fizz and not i % buzz:
            txt_w.write('FB')
            txt_w.write(' ')
        elif not i % fizz:
            txt_w.write('F')
            txt_w.write(' ')
        elif not i % buzz:
            txt_w.write('B')
            txt_w.write(' ')
        else:
            txt_w.write(str(i))
            txt_w.write(' ')
            i += 1
    txt_w.write('\n')
txt.close()
txt_w.close()
