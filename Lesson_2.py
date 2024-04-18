# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
def tasks() -> callable:
    list_tasks: list[str] = []

    def write_task() -> None:
        nonlocal list_tasks
        number_of_tasks: int = int(input("Enter number of tasks: "))
        for i in range(number_of_tasks):
            task: str = input("Enter any task:")

            list_tasks.append(task)

    def display_tasks() -> list[str]:
        nonlocal list_tasks
        print(list_tasks)
        return list_tasks

    return write_task, display_tasks


write_task, display_tasks = tasks()

write_task()

display_tasks()

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# Приклад:

# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4)створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій
