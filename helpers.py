import time


def timer(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        r = f(*args, **kwargs)
        print(f'Function {f.__name__} executed in {(time.time() - t):.3f} s')
        return r
    return wrapper
