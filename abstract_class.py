"""Абстрактные классы-не используется для решения практических задач, но используется как шаблон для будующих клаасов или
подклассов"""

from abc import ABC, abstractmethod

"""Перечисление методов классов для получения ошибки при обращении к тем методам которые не были  переопределенны в дочерних
классах"""


class Resource(ABC):
    @abstractmethod  # Такое объявление методов называется сигнатурным - абстрактный метод без имплеминтации(без внутренней логики)
    def read(self):
        pass

    @abstractmethod  # Обязательное наличие методов read and write у наследуемых классов
    def write(self):
        pass


"""Класс с ошибкой - не переопределенны методы абстрактоного класс Resource"""

# class BadFile(Resource):
#     def __init__(self):
#         pass
#
#     def get_data(self):
#         pass
#
#     def put_data(self):
#         pass

"""Класс с переопределенными методами наследуемого аюстрактого класса"""


class BadFile(Resource):
    def __init__(self):
        pass

    def read(self):
        pass

    def write(self):
        pass


my_file = BadFile()

my_file.read()

"""Создание публичных полей в абстрактном классе"""


class BaseCourse(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def credits(self):
        pass


class Course(BaseCourse):
    def __init__(self, title, description, credits):
        self._title = title
        self._description = description
        self._credits = credits

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def credits(self):
        return self._credits

    
course = Course("Title", "Description content", 15)
