import time
import requests

from threadpool_decorator import thread_pool_decorator
from run_time_decorator import run_time_decorator


@run_time_decorator
@thread_pool_decorator(5, True, 0)
def square(x):
    # numbers = [1, 2, 3, 4, 5]
    # for i in numbers:
    #     print(i * i)
    # print()
    return x * x


@run_time_decorator
@thread_pool_decorator(3, True, 0)
def download_page(url):
    response = requests.get(url)
    return response.content


urls = ['https://stackoverflow.com', 'https://google.com', 'https://facebook.com']


if __name__ == '__main__':
    # futures = square([1,2,3,4,5])
    # start = time.time()
    # for url in urls:
    #     print(len(download_page(url)))
    # print(time.time() - start)
    # start = time.time()
    futures = download_page(urls)
    for future in futures:
        try:
            result = future.result()
            print(len(result))
        except Exception as e:
            print(f"Function threw an exception: {e}")

    # print(time.time() - start)