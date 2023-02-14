# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1



def Fibonacci(n, m):

    a = 1
    b = 1
    f_list = [1, ]
    for i in range(m):
        a, b = b, a + b
        f_list.append(a)
    return f_list[n-1:m]
print('Fibonacci(1, 9): ', Fibonacci(1, 9))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()



def sort_to_max(my_list):

    if len(my_list) > 1:
        pivot_index = len(my_list) // 2
        smaller_items = []
        larger_items = []
        for i, val in enumerate(my_list):
            if i != pivot_index:
                if val < my_list[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)
        sort_to_max(smaller_items)
        sort_to_max(larger_items)
        my_list[:] = smaller_items + [my_list[pivot_index]] + larger_items
    return my_list
print(sort_to_max([65, 34.876, 654, 1, 0, -876, -9, 1234, 2.3]))




# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.



def filter_F(function, iterable):
    return (item for item in iterable if function(item))
print(list(filter_F(lambda x: True if x % 2 == 0 else False,
                           [1, 2, 3, 4, 5, 6, 7, 8, 9])))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.



def is_it_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
       abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False