# 2) Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.

import functools, threading, time, os, requests

file_tuple = (
    'https://shiny-diski.com.ua/media/images/Goodyear-Ultra-Grip-Ice--SUV-G1.500x500.jpg',
    'https://shiny-diski.com.ua/media/images/%D0%B4%D1%83%D0%B1%D0%BB%D1%8C_g1234_Q0qBfig.500x500.jpg',
    'https://shiny-diski.com.ua/media/images/%D0%B4%D1%83%D0%B1%D0%BB%D1%8C_g1234_Q0qBfig.500x500.jpg',
    'https://shiny-diski.com.ua/media/images/%D0%B4%D1%83%D0%B1%D0%BB%D1%8C_g12_PHz6ph2.500x500.jpg',
    'https://shiny-diski.com.ua/media/images/%D0%B4%D1%83%D0%B1%D0%BB%D1%8C_g12_PHz6ph2.500x500.jpg',
    'https://shiny-diski.com.ua/media/images/%D0%B4%D1%83%D0%B1%D0%BB%D1%8C_g1_YdLRFAI.500x500.jpg',
)


def decorator(name: str, id_demon: bool, file_tuple: tuple):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for url in file_tuple:
                print(f'Start thread for url: {url}')
                threading.Thread(target=func, args=url, kwargs=kwargs, daemon=id_demon, name=name).start()
                print(f'Stop thread for url: {url}')
            return
        return wrapper
    return actual_decorator


@decorator('download', False, file_tuple)
def file_downloader(url: str = ''):
    print(f'Start download for url: {url}')
    time.sleep(3)
    filepath = os.path.join(os.getcwd() + '/Downloads/')
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    print(f'Stop download for url: {url}')


file_downloader('first', 'second')
