# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def make_first_letter_large(any_word):
    """
    функция получает слово с буквы в нижнем регистре и возращяет его с первой буквой в верхнем
    :param any_word: str
    :return: str
    """
    new_value_el = ord(any_word[0]) - 32
    return f'{chr(new_value_el)}{any_word[1:]}'


my_list_from_str = 'to be or not to be'.split()
new_my_list = ' '.join(list(map(make_first_letter_large, my_list_from_str)))

print(new_my_list)
