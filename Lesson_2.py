# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from typing import Callable, Tuple


def task_keeper() -> Tuple[Callable, Callable]:

    tasks: list[str] = []

    def write_task() -> None:
        nonlocal tasks
        while len(tasks) < 3:
            write_task: str = input("Write a task: ")
            tasks.append(write_task)

    def show_task() -> list[str]:
        nonlocal tasks
        print(tasks)
        return tasks.copy()

    return write_task, show_task


write_task, show_task = task_keeper()
write_task()
show_task()

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expand_form(number: int) -> str:
    new_number = str(number)
    n = len(str(number))
    var: list[str] = []
    for i, elem in enumerate(new_number):
        if elem != '0':
            value = elem + '0' * (n - i - 1)
            var.append(value)

    return ' + '.join(var)


print(expand_form(70304))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decorator(func):

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(count)

    return wrapper


@decorator
def count():
    print('Hello World')


count()
count()
count()
count()
count()
