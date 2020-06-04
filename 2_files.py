"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file_1:
        content = file_1.read()
        len_of_file = len(content)
        word_in_file = len(content.split())
        replace_in_file = content.replace('.', '!')
        list_for_write = [len_of_file, word_in_file, replace_in_file]
        with open('referat2.txt', 'a', encoding='utf-8') as file_2:
            for arg in list_for_write:
                file_2.write(f"{arg} \n")


if __name__ == "__main__":
    main()
