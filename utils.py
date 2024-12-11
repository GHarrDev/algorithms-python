import time

def time_it(func):
    duration_ms = 0
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration_ms = (end - start) * 1000
        print(f"Execution time for {func.__name__}: {duration_ms:.6f} ms")
        return result
    return wrapper