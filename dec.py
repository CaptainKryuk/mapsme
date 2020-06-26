# Напиши декоратор, который считает количество вызовов произвольной функции и при превышении лимита, передаваемого параметром, выбрасывает исключение.(приложить ссылочку на код)
import logging
logging.basicConfig(level=logging.INFO)

from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def storage():
    total = 0
    while True:
        yield
        total += 1
        logging.info("was called {} times.".format(total))

store = storage()

def count(func):
    def wrapper(*args, **kwargs):
        store.send(1)
        return func(*args, **kwargs)
    return wrapper

        
@count
def func():
    logging.info("Function was called.")


for i in range(int(input("Количество вызовов func():"))):
    func()



