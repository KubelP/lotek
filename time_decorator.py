import time

def time_measure(func):

    """
    Decorator for measure time elapsed from start to end of function.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        delta = int((end - start))
        print(f'Program worked by {delta}s')
    return wrapper
