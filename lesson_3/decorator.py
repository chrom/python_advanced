# Создать декоратор, который принимает на вход аргумент «количество повторений».
# Который будет вызывать функцию, определенное кол-во раз.
# Декорируемая функция должна возвращать:
# 1) Количество времени затраченное на каждый вызов;
# 2) Количество времени затраченное в общей сложности на все вызовы;
# 3) Имя декорируемой функции;
# 4) Значение последнего результата выполнения.
import functools
import time


def decorator(number):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            function_call = {}
            start_time_all = time.perf_counter_ns()
            for i in range(0, number + 1):
                start_time_call = time.perf_counter_ns()
                result = func(*args, **kwargs)
                end_time_call = time.perf_counter_ns()
                print(end_time_call - start_time_call)
                function_call[i] = end_time_call - start_time_call

            stop_time_all = time.perf_counter_ns()
            run_time = stop_time_all - start_time_all

            return f'Finished function {func.__name__!r} in {run_time:.4f} ns \n ' \
                   f'Each function call:  {function_call} \n' \
                   f'Last result: {result}'

        return wrapper

    return actual_decorator


@decorator(18)
def target_function(name):
    return f'Hello world, {name}'


print(target_function('This is the root!'))
