# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
def notebook() -> list:
    todo_list: list = []

    def add_todo(todo: str) -> list:
        todo_list.append(todo)
        return todo_list

    def all_todo() -> list:
        nonlocal todo_list
        return todo_list

    return [add_todo, all_todo]


add, all = notebook()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def counter(func):
    counter = 0

    def inner(*args, **kwargs):
        nonlocal counter
        counter = counter + 1
        print(f'Функция вызвана {counter} раз')
        print('*' * 20)
        res=func(*args, **kwargs)
        return res
    return inner


@counter
def expanded_form(a: int) -> str:
    b = list(str(a))
    res = [c for c in b]
    i = 0
    l = len(res)
    while i < l + i:
        if res[i] != '0':
            res[i] = res[i] + '0' * (l - 1)
        else:
            res[i] = ' '

        l = l - 1
        i = i + 1

    return '+'.join(res).replace('+ ', '')


@counter
def hello(name):
    print(f'Hello {name}')


@counter
def foo():
    return (5)


print(expanded_form(12312))
print(expanded_form(4070))
print(expanded_form(400899))
print(expanded_form(12))

hello('max')
hello('max')
hello('max')
hello('max')
hello('max')