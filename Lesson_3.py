# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    __slots__ = 'side_x', 'side_y', 'area'

    def __init__(self, side_x, side_y):
        self.side_x = side_x
        self.side_y = side_y
        self.area = side_x * side_y

    def __mul__(self, other):
        return self.area * other.area

    def __add__(self, other):
        return self.area * other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return self.side_x * 2 + self.side_y * 2


rectangle1 = Rectangle(8, 5)
rectangle2 = Rectangle(5, 6)
print(len(rectangle1))


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):

    count = 0

    def __init__(self, name, age, size):
        super().__init__(age, name)
        self.size = size
        Cinderella.count += 1

    @classmethod
    def sum_count(cls):
        print(cls.count)


class Prince(Human):

    def __init__(self, name, age, shoes_size):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.size == self.shoes_size:
                print(cinderella)
                return cinderella
            else:
                print('Not suitable shoes')


cinderella1: [Cinderella] = [Cinderella('lisa', 20, 38),
                             Cinderella('nika', 21, 35)]
prince = Prince('john', 20, 38)
prince.find_cinderella(cinderella1)
