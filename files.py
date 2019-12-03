"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt','r',encoding='utf-8') as f_in:
        content = f_in.read()
        print('String length:',len(content))
        print('Word count:',len(content.split(' ')))
    with open('referat2.txt','w',encoding='utf-8') as f_out:
        f_out.write(content.replace('.','!'))


if __name__ == "__main__":
    main()
