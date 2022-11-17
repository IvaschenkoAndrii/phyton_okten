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
        return self.a*self.b+other.a*other.b

    def __sub__(self, other):
        if self.a * self.b>other.a * other.b:
            return self.a * self.b - other.a * other.b
        else:
            return other.a * other.b-self.a * self.b

    def __eq__(self, other):
        return other.a * other.b==self.a * self.b

    def __ne__(self, other):
        return other.a * other.b != self.a * self.b

    def __lt__(self, other):
        return other.a * other.b < self.a * self.b

    def __gt__(self, other):
        return other.a * other.b > self.a * self.b

    def __len__(self):
        return (self.a+self.b)*2


rectangle = Rectangle(2, 4)
rectangle2 = Rectangle(3, 4)

print(rectangle2!=rectangle)

