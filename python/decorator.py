# -*- coding: utf-8 -*-
"""
Created on 2024-12-13 10:59:22

@author: .v, Chairman of sigma.lab.

I hope to use AI or LLMs to help people better understand the world and humanity.

We are big fans of xAI.

I am recently interested in MLLMs' safety and Multi-Agent.
"""

import time


def test_decorator(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        result = func(*args, **kwargs)
        print('Call finished, 调用hello_world()的时候实际上调用的是wrapper函数.')
        return result
    return wrapper


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


class Timer:
    """
    '!r' 在这里指的是输出string的repr形式, \n
    比如 a = 'str', \n
    那么 print(f"{a}") 得到 st, print(f"{a!r}") 得到 'st'.
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Function {self.func.__name__!r} took {end - start:.3f} seconds to execute.")
        return result


timer_decorator = Timer


# 用函数作装饰器
@test_decorator
def hello_world():
    print('Hello World!')


# 用类作装饰器
@CountCalls
def hello_world_counts():
    print('Hello World!')


def run_many_times(func, times):
    for _ in range(times):
        func()


# 用实例做装饰器
@timer_decorator
def test_sleep_process():
    time.sleep(1.23)


if __name__ == '__main__':
    # hello_world()
    # run_many_times(hello_world_counts, 3)
    test_sleep_process()
