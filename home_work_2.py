str_1 = 'gto Python well in hi php go to the C C in a dyn'

stop_word = ["Python", 'php', 'go', 'C']


# def delete_stop_word(str_0):
#     list_split_str = str_0.split(' ')
#
#     # for word in stop_word:
#     #     if word in list_split_str:
#     #         list_split_str.remove(word)
#     # return " ".join(list_split_str)
#
#     return " ".join(filter(lambda word: word not in stop_word, list_split_str))
#
#
# print(delete_stop_word(str_1))


# 2.Имеется список, состоящий из чисел.
# Напишите функцию которая принимает число и возвращает
# список состоящий из элементов первого списка кратных входному параметру.

num_1 = [1, 2, 3, 4, 6]


# def my_func_2(list_0, num):
#     return list(filter(lambda x: x % num == 0, list_0))
#
#
# print(my_func_2(num_1, 2))


# 3. Напишите функцию, которая принимает любое количество не именованных аргументов
# и возвращает кортеж состоящий из аргументов у которых тип данных str


# def arg_func(*args):
#     return tuple(filter(lambda x: type(x) == str, args))
#
#
# print(arg_func(1, 55, 'a', 'asd',))


# 4. Имеются два списка состоящие из произвольных элементов.
# Напишите функцию которая возвращает пересечение списков (элементы которые встречаются в и там и там)


# def func_3(list_1, list_2):
#     return list(filter(lambda x: x in list_2, list_1))
#
#
# print(func_3([3,5, 'a', [2]], [3, 'd', 'a', [2]]))


# 5. Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
# -	Длина каждой ступени может отличаться.
# -	n - натуральное число в диапазоне от 1 до 100.

#
# def lesenka(bricks_quantity, stupen_1, LEN):
#     stupen_LIST = []
#     stupen_LIST.append(stupen_1)
#     stupen = stupen_LIST[0]
#     stupen_quantity = 0
#     lesenka_quantity = 0
#     while bricks_quantity >= 0:
#         bricks_quantity -= stupen
#         stupen -= LEN
#         stupen_quantity += 1
#         if stupen < 1:
#             stupen = stupen_LIST[0]
#             lesenka_quantity += 1
#     return lesenka_quantity
#
#
# print(lesenka(10, 5, 1))


# 6.	Напишите декоратор который выводит исключение
# в случае если декорируемая функция возвращает тип данных отличный от int
# Напишите 2 тестовые декорируемые функции с произвольными данными


# def decor_exception(func):
#     def internal(args):
#         result = func(args)
#         if type(result) is not int:
#             raise Exception("Тип данных отличный от int!")
#         else:
#             return func(args)
#     return internal
#
#
# @decor_exception
# def test_func_1(arg_1):
#     return arg_1+2
#
#
# @decor_exception
# def test_func_2(arg_2):
#     return arg_2*2
#
#
# print(test_func_1(55))
#
# print(test_func_2(55.1))


# 7.	Напишите декоратор который запускает декорируемую функцию повторно,
# в случае если произошло исключение при первом запуске.
# Напишите 2 тестовые декорируемые функции с произвольными данными.


def decor_recode(func_2):
    def internal_func(arg):
        try:
            return func_2(arg)
        except:
            return func_2(arg)
    return internal_func


@decor_recode
def func_error(a):
    return 1/a


@decor_recode
def func_plus_1(a):
    return 1 + a


print(func_plus_1(0))
print(func_error(0))

