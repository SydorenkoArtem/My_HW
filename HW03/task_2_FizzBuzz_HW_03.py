# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

# открываем файл на чтение (опция 'r')
txt = open('task_2_fizzbuzz_hw03.txt', 'r')  # в файле теперь file descriptor

for line in txt:  # для каждой строки в файле
	list = line.split()  # строку из файла формируем в список
	fizz = int(list[0])
	buzz = int(list[1])
	number = int(list[2])

	for i in range(1, number + 1):
		if i % fizz == 0 and i % buzz == 0:
			print('FB', end=' ')
		elif i % fizz == 0:
			print('F', end=' ')
		elif i % buzz == 0:
			print('B', end=' ')
		else:
			print(i, end=' ')
			i += 1
	print(end='\n')
txt.close()  # закрытие файла
