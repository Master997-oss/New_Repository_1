import re
import random
import pathlib
from pathlib import Path




# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# print(line)

# Решение задачи с помощью модуля "re"

line_string = re.findall(r'[a-z]+', line)
print('Все символы из исходных строк в нижнем регистре с использованием модуля re: \n', line_string)



# Решение без модуля "re"

symbol = list(map(lambda x: chr(x), list(range(65, 91))))
line_new_0 = list(line)

for i, n in enumerate(line_new_0[:]):
       for d in symbol:
              if n == d:
                     line_new_0[i] = ' '

stroka_new = ''.join(line_new_0).split(' ')

line_str_2 = [i for i in stroka_new if i != '']
print('Все символы из исходных строк в нижнем регистре без использования модуля re: \n', line_str_2, '\n')





# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


# Решение задачи с помощью модуля "re"

line_2_string = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('Преобразованный список с использованием модуля re: \n', line_2_string)


# Решение без модуля "re"

symb1 = list(map(lambda x: chr(x), list(range(65, 91))))
symb2 = list(map(lambda x: chr(x), list(range(97, 123))))
line_new_2 = list(line_2)

lst = []
i = len(line_new_2) - 1

while i >= 0:
       if line_new_2[i] in symb2:
              lst.append(line_new_2[i])
       elif line_new_2[i] in symb1 and i <= len(line_new_2) - 3 and line_new_2[i + 1] in symb1 and line_new_2[
              i + 2] in symb1:
              lst.append(line_new_2[i])
       else:
              lst.append(' ')
       i -= 1
lst.reverse()

i = 0
lst2 = []
registr = True

while i <= len(lst) - 1:
       if lst[i] in symb2:
              registr = True
       if lst[i] in symb1 and lst[i - 1] in symb2 and lst[i - 2] in symb2:
              lst2.append(lst[i])
              registr = False
       elif lst[i] in symb1 and registr == False:
              lst2.append(lst[i])
       else:
              lst2.append(' ')
       i += 1
stroka = ''.join(lst2).split(' ')

line_str_3 = [i for i in stroka if i != '']
print('Преобразованный список без использования модуля re: \n', line_str_3, '\n')





# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


max_num = 2500

my_list = [random.randint(0, 9) for _ in range(max_num)]
spisok = ''.join(list(map(lambda x: str(x), my_list)))

print(my_list)

path = r'C:\Users\User\Desktop\git_exercise\New_Repository_1\lesson_5\script.txt'
with open(path, 'w', encoding='UTF-8') as file:
       file.write(str(my_list))

with open(path, 'r', encoding='UTF-8') as file:
       string_1 = list(file.read())
print(string_1)

n = (random.randint(0, 9) for i in range(2500))
str = ''.join(str(i) for i in n)

with open('script.txt', 'w', ) as f:
       f.write(str)
       found = re.findall(r'[0-9]', str)
       print(found)


