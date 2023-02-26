import time
import os
from colorama import *

x = 0

login = os.getlogin()

print(Fore.GREEN + '\nMoreMkDir v2.0 made by @ryzenkz\n\nМассовый создатель папок с плюшками\n')

directory = input('Путь до папки (По умолчанию C:/Users/' + login + '/Desktop/ ):\n')
   
if directory == '':
   directory = 'c:/Users/' + login + '/Desktop/' + 'folders'
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


print(Fore.GREEN + '\nГотово!!\n', 'Создано', i, 'папок')
