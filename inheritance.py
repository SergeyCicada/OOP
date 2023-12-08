"""Новый класс на базе имеющегося - наследование
1. Расширение существующего класса
2. Изменение работы класса без его переписывания
3. Создание цепочки связанных классов для комбинирования  функционала нескольких классов в одном"""

"""1."""


class Book:
    def __init__(self, name, pages, content, author):
        self.name = name
        self.pages = pages
        self.content = content
        self.author = author


class Ebook(Book):
    def __init__(self, name, pages, content, author, links):
        super().__init__(name, pages, content, author)
        self.links = links


book_1 = Book("Книга Python", 300, "", "Я")
book_2 = Ebook("Книга Python", 300, "", "Я", ["https://library.io/book/006.pdf"])

"""2."""


class StoreItem:
    def calculate(self, count):
        return self._calculate_tax(count) + (count * 100)

    def _calculate_tax(self, count):
        return 0


class StoreItemInternational(StoreItem):
    def _calculaete_tax(self, count):
        return count * 0.5


item = StoreItemInternational()
item.calculate(10)

"3."


class PrintedProduct:
    def __init__(self, name, pages, content):
        self.name = name
        self.pages = pages
        self.content = content


class Book(PrintedProduct):
    def __init__(self, name, pages, content, author):
        super().__init__(name, pages, content)
        self.author = author


class Magazine(PrintedProduct):
    def __init__(self, name, pages, content):
        super().__init__(name, pages, content)