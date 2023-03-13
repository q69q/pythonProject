def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Количество строк целое число, положительное')
# Проверка
read_last(4, 'article.txt')
read_last(-2, 'article.txt')