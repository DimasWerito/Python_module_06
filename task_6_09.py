"""
Реалізуйте функцію get_credentials_users(path), 
яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. 
Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
"""


def get_credentials_users(path):
    with open(path, "rb") as f:
        lines = f.readlines()
        result_list = []
        for line in lines:
            line_decoded = line.decode().replace("\n", "")
            result_list.append(line_decoded)
        return result_list
        