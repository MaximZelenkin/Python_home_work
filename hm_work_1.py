# --------------Task 1--------------------
#
# def LenStr(str_1=''):
#     if isinstance(str_1, str):
#         len_1 = len(str_1)
#     else:
#         len_1 = 'Это не строка'
#     return len_1
#
#
# print(LenStr())
#

# --------------Task 2--------------------

# def MaxList(list_1=[], list_2=[]):
#     if isinstance(list_1, list) and isinstance(list_2, list):
#         if len(list_1) > len(list_2):
#             return list_1
#         elif len(list_2) > len(list_1):
#             return list_2
#         else:
#             return "Списки равны"
#     else:
#         return 'Хотябы один из аргументов не список'
#
#
# print(MaxList([123], [1]))


# --------------Task 3--------------------

# def AddArgforList(list_1=[], arg=0):
#     list_1.append(arg)
#     return list_1
#
#
# print(AddArgforList([1, 2, 3], ))


# --------------Task 4--------------------


# def FuncNum(x=0):
#     if -100 <= x <= 100:
#         return '+'
#     else:
#         return '-'
#
#
# print(FuncNum())


# --------------Task 5--------------------


def FuncControl(str_1='test', str_2='test1'):
    if str_1 in str_2:
        return "ДА"
    else:
        return "НЕТ"


print(FuncControl('d','def'))


# --------------Task 6--------------------

# def func():
#     pass
#
#
# print(func())


# --------------Task 7--------------------


# def func():
#     pass
#
#
# print(func())


# --------------Task 8--------------------


# def func():
#     pass
#
#
# print(func())


# --------------Task 9--------------------


# def func():
#     pass
#
#
# print(func())


# --------------Task 10--------------------

lst = [2, 4, 5, 8, 9, 13]

def func(list_1):
    i = 0
    new_list = []
    while i < len(list_1):
        num = list_1[i] * i
        new_list.append(num)
        i += 1
    return new_list


print(func(lst))

