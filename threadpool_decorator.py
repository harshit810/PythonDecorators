from functools import wraps
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor


def thread_pool_decorator(max_workers=5, use_iterable=False, iterable_index=0):
    '''
        Method to run the thread pool executor
        :param max_workers: number of threads to run
        :param use_iterable: whether to use iterable object for method calling
        :param iterable_index: the index of the argument to treat as an iterable
    '''

    def thread_pool_executor(func):
        '''
            Run the function using threads
            :returns: a list of concurrent.futures.Future objects, each representing the execution of the function in a separate thread    
        '''

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("threads ", max_workers)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                if use_iterable and isinstance(args[iterable_index], Iterable):
                    futures = [
                        executor.submit(
                            func, 
                            *(args[: iterable_index] + (item, ) + args[iterable_index + 1: ]),
                            **kwargs
                        ) for item in args[iterable_index]
                    ]
                else:
                    futures = [
                        executor.submit(
                            func,
                            *args, 
                            **kwargs
                        ) for _ in range(max_workers)
                    ]
            
                return futures
        
        return wrapper
    return thread_pool_executor