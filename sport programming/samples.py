import re

name = input('Your Name: ')

names = ['Ilya', 'Ali', 'Nikita', 'Serega']

text = 'Привет как дела что делаешь'

res = re.search(name, text)

print(res.group())