import ctypes

# Загрузка библиотеки DLL
dll_master = ctypes.CDLL(r"../dll_master/x64/Debug/dll_master.dll")

# Вызов функции из DLL

helloWorld = dll_master.helloWorldExport() # проблема с типом данных, сделал по тупому
total = dll_master.totalExport(2, 3)
#echo = dll_master.echoExport(input()) # проблема с памятью 

# Вывод результата
#print(helloWorld)
print('\n', total)
