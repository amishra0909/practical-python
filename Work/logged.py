# logged.py

def logged(func):

    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        func(*args, **kwargs)

    return wrapper


def add(x, y):
    return x + y


if __name__ == '__main__':
    logged_add = logged(add)
    print(logged_add(3, 5))
