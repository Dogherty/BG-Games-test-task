from typing import Union
def get_next_sequence(input_data: Union[str, list]) -> list:
    # Проверяем, состоит ли последовательность из цифр
    if isinstance(input_data, str):
        if any(char.isalpha() for char in input_data):
            raise ValueError('Последовательность должна состоять из цифр')

    # Преобразуем строку в список, если входные данные не являются списком
    if not type(input_data) is list:
        input_data = list(map(int, input_data.split()))

    # Проверяем длину последовательности
    if len(input_data) < 2:
        raise ValueError('Длина последовательности должна быть больше 1')

    # Получаем разности
    d1 = [input_data[i + 1] - input_data[i] for i in range(len(input_data) - 1)]
    d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
    d3 = [d2[i + 1] - d2[i] for i in range(len(d2) - 1)]

    # Если разности пустые (слишком короткая последовательность), то добавляем 0
    if d3 == []:
        d3.append(0)
    if d2 == []:
        d2.append(0)

    # Получаем первую разность последовательности
    sequence = [d1[-1] + d2[-1] + d3[-1]]

    # Получаем вторую и третью разности последовательности
    for i in range(2):
        sequence.append(sequence[-1] + d2[-1] + d3[-1])

    # Получаем последние три элемента исходной последовательности
    s_M = input_data[-1]
    s_M1 = s_M + sequence[0]
    s_M2 = s_M1 + sequence[1]
    s_M3 = s_M2 + sequence[2]

    return [s_M1, s_M2, s_M3]

# Простой тест, вместо unittest
def testing(input_data: Union[str, list], output_data: Union[str, list]) -> bool:
    # Преобразуем строку в список, если входные данные не являются списком
    if not type(input_data) is list:
        input_data = list(map(int, input_data.split()))
    if not type(output_data) is list:
        output_data = list(map(int, output_data.split()))

    # Сравниваем полученные данные с ожидаемыми
    if output_data == get_next_sequence(input_data):
        return True
    else:
        raise ValueError(f'Ожидалось: {output_data}\n'
                         f'Получено: {get_next_sequence(input_data)}')

if __name__ == '__main__':
    # Тестовые данные
    in_list = ['12 14 16 18 20', '15 32 57 90 131 180', '1 1 1 1 1']
    out_list = ['22 24 26', '237 302 375', '1 1 1']

    # Запускаем тесты
    for i in range(len(in_list)):
        print(f'Вход: {in_list[i]}\n'
              f'Выход: {out_list[i]}')
        print(f'Результат: {testing(in_list[i], out_list[i])}\n')

    # Ввод своих данных

    # input_data = input('Введите последовательность чисел через пробел: ')
    # print(f'Следующие три числа последовательности: {get_next_sequence(input_data)}')