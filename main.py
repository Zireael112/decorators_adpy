import time
from trace import tracking
from trace_way import find_way
from for_test import url_hulk, take_int

PATH = 'logs/logs.log'

# Use first decorator
@tracking
def squaring(a, b):
    res = a ** b
    time.sleep(2)
    return res


squaring(3, 4)

# Use second decorator
@find_way(PATH)
def squaring(a, b):
    res = a ** b
    time.sleep(2)
    return res


squaring(4, 3)
