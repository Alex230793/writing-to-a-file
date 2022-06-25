file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_4 = '4.txt'


def file_work(file_name): # функция чтения
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def number_of_rows(file_name): # функция подсчета кол_ва строк
    with open(file_name, 'r', encoding='utf-8') as file:
        rows = len(file.readlines())
        print(f'Количество строк в {file_name} - {rows}')
        return rows


def file_app(file_name, file_append): # функция добавления данных (1 аргумент - файл в который хотим записать, 2 - файл из которого берем информацию)
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'Имя файла - {file_append}\nКоличество строк - {number_of_rows(file_append)}\n\n{file_work(file_append)}\n\n')


# print(number_of_rows(file_1))
# print(number_of_rows(file_2))
# print(number_of_rows(file_3))

file_app(file_4, file_2)
file_app(file_4, file_1)
file_app(file_4, file_3)


