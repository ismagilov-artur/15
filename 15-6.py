def print_document(pages):
    for page in pages:
        if page.startswith("Секретно "):
            print('Дальнейшие материалы засекречены')
            return
        print(page, end='\n')
    print('Напечатано без купюр')

print_document(["Обычная страница", "Иеще страница", "Секретно Вот этот воттекст не показывать", "Никому",
"Никогда"])