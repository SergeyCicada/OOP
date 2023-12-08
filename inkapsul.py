"""1.Инкапсуляция методов класса _, __. Скрытие методов, полей класса за интерфейсом и предоставление интерфейса для
взаимодествия с ними.
Интерфейс класса - набор методов доступный из вне класса"""


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, old_password, new_password):
        self._is_password_correct(old_password)
        self.__is_password_valid(new_password)
        self._was_password_used(new_password)

    def _is_password_correct(self, old_password):  # Защищенный метод / protected / недоступны снаружи, но доступны внутри класса и для потомков
        pass

    def __is_password_valid(self, new_password):  # Приватный метод / private / недоступны снаружи, недоступны для потомков, но доступны внутри класса
        pass

    def _was_password_used(self, new_password):
        pass


user = User("John", "1234")

user.change_password("123", "123")

"""Инкапсуляция полей класса"""


class Player:
    def __init__(self):
        self._hits = 0  # переменная доступная только внутри класса

    def add_hit(self):
        self._hits += 1


"""2.SETеры и GETеры"""

"""Не правильный подход к ООП"""


class User:
    def __init__(self, name):
        self.name = name


user_1 = User("Artur")
user_1.name = "Artur"

"""Правильнй подход ООП, приватность полей экземляра"""


class User:  # Реализация SETera(изменение данных)
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):  # Реалиация SETera
        self._name = new_name


user_1 = User("Jonh")

user_1.set_name("Artur")


class User:  # Реализация GETera(получения)
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


user_1 = User("John")

"""Реализация хранения полей в классе, согласно ООП, GETeram and SETeram"""


class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):  # Geter
        return self._name

    def set_name(self, new_name):  # Setter
        self._name = new_name


"""3. _@property_ and _@setter, упрощение работы с полями не нарушая принцип работы инкапсуляции"""


class Cat:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


cat = Cat("Barskih")

name = cat.name
# print(name)


class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


student = Student("Johan", 2)

student_course = student.course

student.course = 1
student.name = "Mice"


