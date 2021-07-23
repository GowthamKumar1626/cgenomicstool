import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken to run this", func.__name__,f"is {end-start}")
        return result
    return wrapper


def try_except(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error From:\t{func.__name__}.\nMessage:\t{e}")
    return wrapper

