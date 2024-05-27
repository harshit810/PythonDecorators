import time
import functools
import sys
import os
import psutil


def run_time_decorator(func):
    '''
        Method to get the run time and other details of a function
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Function name
        print(f"Function name: {func.__name__}")
        # Arguments
        print(f"Arguments: {args}")
        # Keyword arguments
        print(f"Keyword arguments: {kwargs}")
        # Start time
        start = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Function threw an exception: {e}")
            result = None
        # End time
        end = time.time()
        # Running time
        print(f"Running time: {end - start} seconds")
        # Memory usage
        process = psutil.Process(os.getpid())
        print(f"Memory usage: {process.memory_info().rss / 1024**2} MB")
        # Return value
        print(f"Return value: {result}")
        return result
    
    return wrapper
