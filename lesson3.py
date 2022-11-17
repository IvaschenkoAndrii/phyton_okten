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


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size


class Cindirella(Human):
    count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cindirella.count = Cindirella.count+1

    @classmethod
    def get_count(cls):
        print(cls.count)


