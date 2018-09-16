# https://habr.com/post/187482/
import psutil
from time import time

'''
def timed(fn):
    def decorated(*x):
        start = time()
        result = fn(*x)
        print ("Executing %s took %d ms" % (fn.__name__, (time() - start)*1000))
        return result
    return decorated'''

''' 
https://stackoverflow.com/questions/49376371/python-decorators-args-and-kwargs
#import functools, logging

def tracing(func):
    @functools.wraps
    def wrapper(*args, **kwargs):
        logging.debug(f'Calling {func.__name__}')
        try:
            return func(*args, **kwargs)
        finally:
            logging.debug(f'Called {func.__name__}')
    return wrapper

@tracing
def spam():
    print('spam')

@tracing
def add3(n):
    return n+3
    
the reason we need to take *args, **kwargs is so that we can pass that same *args, **kwargs on to the wrapped function.
This is called "forwarding", or "perfect forwarding". The idea is that "tracing" doesn't have to know anything about 
the function it's wrapping—it could take any set of positional and keyword arguments, and return anything, and the wrapper still works'''



def repeat(times):
    """ повторить вызов times раз, и вернуть среднее значение """
    def decorator(fn):
        def decorated2(*x):
            total = 0
            for i in range(times):
                total += fn(*x)
            return total / times
        return decorated2
    return decorator

@repeat(5)
def cpuload():
    load = psutil.cpu_percent()
    print ("cpuload() returns %d" % load)
    return load

print ("cpuload.__name__==" + cpuload.__name__)
print ("CPU load is %d%%" % cpuload())
print(psutil.cpu_stats())
print(psutil.sensors_battery())
#print(psutil.temperature(fahrenheit=False))
#print(psutil.sensors_fans())
