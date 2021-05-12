# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
count_str = 0
with open('text.txt', 'r') as f_obj:
    while True:
        content = f_obj.readline()
        if content:
            len_content_str_list = len(content.split())
            count_str += 1
            print(f'{len_content_str_list} - слов в {count_str} строке')
        else:
            break
print(f'всего строк {count_str}')
