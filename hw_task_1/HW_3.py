# 1.	Создайте класс  прямоугольника. Класс принимает два параметра,
# ширина и высота прямоугольника.
# Создайте два метода:
# -	метод возвращающий площадь прямоугольника
# -	метод возвращающий периметр прямоугольника
import random


# class Rectangle:
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
#
#     def area(self,):
#         return self.b * self.h
#
#     def perimeter(self):
#         return (self.b + self.h) * 2
#
#
# a = Rectangle(5, 6)
# print(a.area())


# 2.	Напишите программу - виртуальную модель процесса обучения.
# В программе должны быть объекты: ученик, учитель, учебные материалы.


class Human:
    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.sex = male


class Teacher(Human):
    quantity_teach_student = 0

    def __init__(self, name, age, male):
        super().__init__(name, age, male)

    def teach(self, name_lesson, *students):
        quantity_students = [*students]
        for student in quantity_students:
            student.take(name_lesson)
            self.quantity_teach_student += 1


class Student(Human):
    def __init__(self, name, age, male):
        self.knowledge = []
        super().__init__(name, age, male)

    def take(self, knowledge_name):
        self.knowledge.append(knowledge_name)

    def __len__(self):
        return len(self.knowledge)

    def forget_random(self):
        if len(self.knowledge) > 0:
            forgot = random.randint(0, len(self.knowledge)-1)
            # print('Забыл ', forgot+1)
            self.knowledge.pop(forgot)
        else:
            pass


class Lecture:
    list_attribute = []

    def __init__(self, *args):
        self.list_attribute += [*args]

    def __len__(self):
        return len(self.list_attribute)


lecture = Lecture('Python', 'Course', 'Math', 'Anon', 'SQL',)

teacher_1 = Teacher('Semenov', 63, 'man')

student_1 = Student('Maxim', 20, 'man')
student_2 = Student('Dima', 27, 'man')
student_3 = Student('Den', 50, 'man')
student_4 = Student('Yana', 35, 'woman')


for name_lesson_0 in lecture.list_attribute:
    teacher_1.teach(name_lesson_0, student_1, student_2, student_4)


print(student_1.knowledge)
print(len(student_1))

student_1.forget_random()
print(student_1.knowledge)
print(len(student_1))

print(student_1.name)

print(student_3.name)
print(student_3.knowledge)
print(len(student_3))

