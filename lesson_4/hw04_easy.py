# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили


km = int(input('Введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)


# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.



def my_round(my_number, N_digits):
    my_number = my_number * (10 ** N_digits)
    if float(my_number) - int(my_number) > 0.5:
         my_number = my_number // 1 + 1
    else:
         my_number = my_number // 1
    return my_number / (10 ** N_digits)
print(my_round(5433.364536, 5))



# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)



def lucky_ticket(ticket_number):
    if len(ticket_number) != 8:
        return False
    first_part = ticket_number[0:4]
    second_part = ticket_number[4:8]
    sum_first_part = 0
    for i in first_part:
        sum_first_part = sum_first_part + int(i)
    sum_second_part = 0
    for i in second_part:
        sum_second_part = sum_second_part + int(i)
    if sum_first_part == sum_second_part:
        return True
    else:
        return False
print(lucky_ticket('45331914'))
