# 1) Создать декоратор, который будет запускать функцию в отдельном потоке.
# Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.
import functools
from threading import Thread
import time


def decorator(name: str, id_demon: bool):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Start Thread')
            thread = Thread(target=func, args=args, kwargs=kwargs, name=name, daemon=id_demon)
            thread.start()
            print('Stop Thread')
            return thread
        return wrapper
    return actual_decorator


@decorator('io_bound', False)
def target_function(first, second):
    print(f'target_function Уснула, Run Thread. {first}, {second}')
    time.sleep(3)
    print(f'target_function Проснулась')


target_function('first', 'second')
