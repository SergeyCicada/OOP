"""Полиморфизм(многообразный)-способ при котором различные объекты с одинаковым интерфейсом или поведением могут быть
взаимосвязанны и взаимозаменяемы. Это свойство системы использовать объекты с одинаковым интерфейсом, без информации о
внутреннем устройстве объекта"""

class TestFile:
    def read(self, file):
        pass

    def write(self, file, lines):
        pass


class JSONFile:
    def read(self, file):
        pass

    def write(self, file, lines):
        pass

file_proc = TestFile()

data = file_proc.read('data.txt')

print(data)