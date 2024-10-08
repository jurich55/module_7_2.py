def custom_write(file_name: str, strings: list):

    strings_positions = {}         # пустой словарь (line_number, line_byte)
    line_number = 1                # первая строка
    file = open(file_name, 'w')    # открываем файл в режиме записи
    for string in strings:         # записываем строку в список strings
        line_byte = file.tell()    # байт начала строки
        file.write(f'{string}\n')  # текущая строка
        strings_positions[(line_number, line_byte)] = string
        line_number += 1
    file.close()
    return strings_positions        # возвращаем словарь

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
    # передаем в функцию ее аргументы
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
