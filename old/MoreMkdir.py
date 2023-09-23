import time
import os
from colorama import *

from progress.bar import IncrementalBar

init(autoreset=True)

x = 0

print(Fore.GREEN + '\nMoreMkDir v2.0 made by @ryzenkz\n\nМассовый создатель папок с плюшками\n')

directory = input('Путь до папки (По умолчанию <рабочий стол юзера>):\n')
   
if directory == '':
   directory = 'c:/Users/dyudy/Desktop/' + 'folders'
   os.mkdir(directory)



name = input('Название папок (Пустой для разных названий):\n')

if name == '':
   
   local = input('Введите названия папки:\n')

   directory = directory + '/' + name 
   directory = directory.replace("\\", "/")

   mkdir = directory + local
   
   os.mkdir(mkdir)
   print('Папка '+ local + Fore.GREEN + ' ГОТОВA!')
   i = 1
   i += 1
   

   while local != '':

      local = input('Введите названия папки:\n')
      mkdir = directory + local

      if local != '': 
         os.mkdir(mkdir)
         print('Папкa ' + local + Fore.GREEN + ' ГОТОВA!')
         i += 1
   
   x += 1

elif x < 1:

   stop = int(input("Сколько папок?\n"))
   stop += 1

   directory = directory + '/' + name 
   directory = directory.replace("\\", "/")

   for i in range(1, stop):
      mkdir = directory + str(i)
      os.mkdir(mkdir)
   
   print(Fore.GREEN + '\nДанные приняты\n')

listik = [0] * i

bar = IncrementalBar('Создание папок', max = len(listik))
timer = 1
for item in listik:
    bar.next()
    timer = timer / 2
    time.sleep(timer)

bar.finish()

print(Fore.GREEN + '\nГотово!!\n', 'Создано', i, 'папок')
