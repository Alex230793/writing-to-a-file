from pprint import pprint

file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_4 = '4.txt'
list_of_files = [file_1, file_2, file_3]

# def file_work(file_name): # функция чтения
#     with open(file_name, 'r', encoding='utf-8') as file:
#         return file.read()


def number_of_rows(file_name): # функция подсчета кол_ва строк
    with open(file_name, 'r', encoding='utf-8') as file:
        rows = len(file.readlines())
        # print(f'Количество строк в {file_name} - {rows}')
        return rows

# открывает все файлы которые есть и добавляет их в выбраный файл
def file_app_read(file_date, file_app):
    """
    :param file_date: - список с файлами
    :param file_app: файл в который записываем информацию
    :return: файл с указание названия, количества строк в этом файле, информацию из файла
    """

    list_string_material = {}

    for list_file_date in file_date:
        with open(list_file_date, 'r', encoding='utf-8') as file:
            list_string_material[number_of_rows(list_file_date)] = [list_file_date, file.read()]


    with open(file_app, 'a', encoding='utf-8') as file_a:
        sort_material = sorted(list_string_material.items(), key=lambda x: x[0])
        for position in sort_material:
            file_a.write(f'Имя файла - {position[1][0]}\nКоличество строк - {position[0]}\n\n{position[1][1]}\n\n')




file_app_read(list_of_files, file_4)




