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
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def __add__(self, other):
        return self.a * self.b + other.a * other.b

    def __sub__(self, other):
        if self.a * self.b > other.a * other.b:
            return self.a * self.b - other.a * other.b
        else:
            return other.a * other.b - self.a * self.b

    def __eq__(self, other):
        return other.a * other.b == self.a * self.b

    def __ne__(self, other):
        return other.a * other.b != self.a * self.b

    def __lt__(self, other):
        return other.a * other.b < self.a * self.b

    def __gt__(self, other):
        return other.a * other.b > self.a * self.b

    def __len__(self):
        return (self.a + self.b) * 2


rectangle = Rectangle(2, 4)
rectangle2 = Rectangle(3, 4)


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name


class Cindirella(Human):
    count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cindirella.count = Cindirella.count + 1

    @classmethod
    def get_count(cls):
        print(cls.count)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def search(self, cindirellas):
        res = []
        for i in range(len(cindirellas)):
            if cindirellas[i].foot_size == self.shoe_size:
                res.append(cindirellas[i].name)

        if len(res) != 0:
            return (f"Список подходящих принцесс - {', '.join(res)}")
        return ('Нет подходящих принцесс')


#
p = Prince('s', 22, 38)

cindirellas = [Cindirella('s', 33, 33), Cindirella('a', 33, 34), Cindirella('katya', 33, 33)]

print(p.search(cindirellas))

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book
# або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, item: Book | Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


