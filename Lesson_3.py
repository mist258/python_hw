# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів класу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        res = self.area - other.area
        if res < 0:
            raise ValueError("Area cannot be negative")
        return res

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __len__(self, other):
        return self.x + other.x, self.y + other.y


def main():
    rectangle1 = Rectangle(5, 8)
    rectangle2 = Rectangle(7, 9)
    print(rectangle1 + rectangle2)
    print(rectangle1.__len__(rectangle2))
    print(rectangle2 - rectangle1)
    print(rectangle1 > rectangle2)
    print(rectangle1 < rectangle2)
    print(rectangle1 == rectangle2)
    print(rectangle1 != rectangle2)


if __name__ == '__main__':
    main()


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    @classmethod
    def get_counting(cls):
        return cls.count

    def __str__(self):
        return f'{self.name} {self.age} {self.shoe_size}'


class Prince(Human):
    def __init__(self, name, age, find_shoes):
        super().__init__(name, age)
        self.find_shoes = find_shoes

    def find_cinderella(self, cinderella: list[Cinderella]):
        for cinderella in cinderella:
            if cinderella.shoe_size == self.find_shoes:
                print(cinderella)
                return cinderella

def main():
    cinderella: [Cinderella] = [
        Cinderella('Nika', 18, 38),
        Cinderella('Vika', 20, 40),
        Cinderella('Mila', 25, 39),
        Cinderella('Ira', 22, 37),
        Cinderella('Anny', 30, 36),
        Cinderella('Mary', 38, 35),
    ]
    prince = Prince('Nick', 18, 37)
    prince.find_cinderella(cinderella)

    print(Cinderella.get_counting())


if __name__ == '__main__':
    main()
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine інакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        return f'{self.name}'


class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        return f'{self.name}'


class Main:
    printable_list: list[Book, Magazine] = []

    @staticmethod
    def add(item):
        if isinstance(item, (Book, Magazine)):
            Main.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for items in cls.printable_list:
            if isinstance(items, Book):
                continue
            print(items)

    @classmethod
    def show_all_books(cls):
        for items in cls.printable_list:
            if isinstance(items, Magazine):
                continue
            print(items)


main = Main()
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
# print('-' * 40)
Main.show_all_books()
#
# для перевірки классів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
