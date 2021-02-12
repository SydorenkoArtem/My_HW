python = {'Иванов Иван', 'Андреев Борис', 'Авдеев Иван', 'Мирный Степан', 'Агеев Игорь',
          'Евдокимов Александр', 'Дрокин Александр', 'Береговой Ярослав', 'Сидоренко Артем'}
frontend = {'Евдокимов Александр', 'Дрокин Александр', 'Горняк Иван',
            'Резниченко Илья','Ковш Андрей'}
fullstack = {'Дрокин Александр', 'Мирная Анна', 'Муравьева Татьяна', 'Вольный Борис',
             'Сотая Ирина', 'Евдокимов Андрей', 'Дрокин Степан'}
java = {'Авдеев Иван', 'Мирный Степан', 'Дрокин Александр', 'Мороз Антон', 'Мороз Татьяна',
        'Абросимов Евгений', 'Щебуняев Максим'}
brining_set = python | frontend | fullstack | java
students_without_frontend = brining_set - frontend
java_or_python = python ^ java
students_in_more_groups = python & frontend | fullstack & java | python & fullstack | python & java | \
    frontend & fullstack | frontend & java | fullstack & java

print (students_in_more_groups)
print(students_without_frontend)
print(java_or_python)
