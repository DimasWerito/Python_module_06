"""
Розробіть функцію sanitize_file(source, output), 
що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
"""


def sanitize_file(source, output):
    clean_text = ""
    with open(source, "r") as f:
        text = f.read()
        for el in text:
            if el.isdigit():
                continue
            else:
                clean_text += el
    with open(output, "w") as fh:
        fh.write(clean_text)


def sanitize_file(source, output):
    with open(source, "r") as f:
        text = f.read()
        for l in range(10):
            text = text.replace(f"{l}","")
    with open(output, "w") as fh:
        fh.write(text)