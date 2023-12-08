"""Магические (специальные) методы - методы с двумя подчеркиваниями и автоматическим вызовом  __init__, __repr__"""

class Grade:
    def __init__(self, value=0):  # Инициализатор
        self._value = value

    def __repr__(self):  # Магический метод который вызывается при print(экзмепляр_класса)
        return f"Оценка: {self._value}"

    @property
    def value(self):
        return self._value

    def __eq__(self, other):  # сравнение двух объектов по значениям
        return self.value == other.value

    def __gt__(self, other):  # проверка больше чем
        return self.value > other.value

grade_1 = Grade(3)
grade_2 = Grade(3)

print(grade_1 < grade_2)
