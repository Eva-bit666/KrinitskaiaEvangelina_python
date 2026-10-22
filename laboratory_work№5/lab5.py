#Вариант 1
#Задание 1
import re

text = open("task1-en.txt", encoding="utf-8").read()

result_words = re.findall(r"\b[A-Za-z]{3,5}\b", text)
result_numbers = re.findall(r"\b\d{4,}\b", text)

print(result_words)
print(result_numbers)

#Задание 2
import re

f2 = open('task2.html', errors='ignore').read()
pattern_tags = r'<(?!/|!)[a-zA-Z][^<>]*>'
result_tags = re.findall(pattern_tags, f2)
result_unique = list(dict.fromkeys(result_tags))

print(result_unique)
#Задание 3
import re
import csv

with open('task3.txt') as file:
    FileName = 'users.csv'
    file = file.read()

    pattern_ID = r'(?<![-\d])\b\d{1, 3}\b(?!-)'
    pattern_email = r'\b[\w.+-]+@[\w-]+\.[\w.-]+\b'
    pattern_date = r'\b\d{4}-\d{2}-\d{2}\b'
    pattern_name = r'\b[A-Z][a-z]+\b'
    pattern_link = r'\bhttps?://\S+\b'

    email_list = re.findall(pattern_email, file)
    date_list = re.findall(pattern_date, file)
    name_list = re.findall(pattern_name, file)
    link_list = re.findall(pattern_link, file)
    ID_list = re.findall(pattern_ID, file)

    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(ID_list)):
            row = [ID_list[i], name_list[i], email_list[i], date_list[i], link_list[i]]
            writer.writerow(row)

    with open(FileName, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('; '.join(row))
#Доп задание
import re
with open('task_add.txt', errors='ignore') as file:
    file = file.read()

    pattern_email = r'(?<=\s)[\w.+-]+@[\w-]+\.[a-zA-Z]{2,6}'
    pattern_date = r'(?<=\s)\d{1,4}[-./]\d{1,2}[-./]\d{1,4}'
    pattern_link = r'(?<=\s)https?://[A-Za-z0-9.-]+\.[a-z]{2,6}'

    email_list = re.findall(pattern_email, file)
    date_list = re.findall(pattern_date, file)
    link_list = re.findall(pattern_link, file)

    print(email_list, len(email_list))
    print(date_list, len(date_list))
    print(link_list, len(link_list))