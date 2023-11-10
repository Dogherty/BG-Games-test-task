from typing import Union
def encrypt(key: list, text: list) -> str:
    # Создаем список с ключами из цифр ключа
    key = [int(i) for i in key]
    if len(key) != len(set(key)):
        raise ValueError('Ключ должен состоять из уникальных цифр')

    i = 0
    out = []

    # Разбиваем текст на диграфы и одиночные буквы
    while i < len(text):
        if i + 2 < len(text):
            out.append(text[i:i+2])
            i += 2
        else:
            out.append(text[i:])
            break
        if i < len(text):
            out.append(text[i])
            i += 1

    # Создаем словарь с ключами из цифр ключа
    out_dict = {k: [] for k in key}

    # Заполняем словарь
    for i, value in enumerate(out):
        out_dict[key[i % len(key)]].append(value)

    # Сортируем ключи и объединяем значения словаря в строку
    result = ''.join(''.join(out_dict[k]) for k in sorted(key))
    return result

def decrypt(key: list, text: list) -> str:
    # Создаем список с ключами из цифр ключа
    key = [int(i) for i in key]
    if len(key) != len(set(key)):
        raise ValueError('Ключ должен состоять из уникальных цифр')

    i = 0
    out = []

    # Разбиваем текст на диграфы и одиночные буквы
    while i < len(text):
        if i + 2 < len(text):
            out.append(text[i:i+2])
            i += 2
        else:
            out.append(text[i:])
            break
        if i < len(text):
            out.append(text[i])
            i += 1

    # Создаем словарь с ключами из цифр ключа
    out_dict = {k: [] for k in key}

    # Заполняем словарь
    for i, value in enumerate(out):
        out_dict[key[i % len(key)]].append(value)

    # Сортируем ключи и объединяем значения словаря в строку
    result = ''.join(''.join(out_dict[k]) for k in key)
    return result
# Простой тест, вместо unittest
def testing(text_in: Union[str, list], text_out: Union[str, list]) -> bool:
    key, text = text_in.split(' ', 1)

    # Удаляем пробелы из текста если они есть
    if ' ' in text:
        text = text.replace(" ", "")

    # Получаем зашифрованный текст
    encrypted_text = encrypt(key, text)

    # Сравниваем полученные данные с ожидаемыми
    if text_out == encrypted_text:
        return True
    else:
        raise ValueError(f'Ожидалось: {text_out}\n'
                         f'Получено: {encrypted_text}')

if __name__ == '__main__':
    # Тестовые данные
    in_list = ['41325 INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS', '12 HELLOWORLD', '3412 THISISJUSTATEST', '165432 WORKSMARTNOTHARD', '231 LLOHE']
    out_list = ['CECRTEGLENPHPLUTNANTEIOMOWIRSITDDSINTNALINESAALEMHATGLRGR', 'HELOORDLWL', 'SITASTTHJUESIST', 'WONOTARDMRKSHART', 'HELLO']

    # Запускаем тесты
    for i in range(len(in_list)):
        print(f'Вход: {in_list[i]}\n'
              f'Выход: {out_list[i]}')
        print(f'Результат: {testing(in_list[i], out_list[i])}\n')

    # Ввод своих данных

    key, text = input('Введите ключ и предложение для шифра (Пример: 1245 HELLOWORLD): ').split(' ', 1)
    if ' ' in text:
        text = text.replace(" ", "")
    print(f'зашифрованное сообщение: {decrypt(key, text)}')

