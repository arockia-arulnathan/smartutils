from smartutils.timeutil import get_exec_time
import time


@get_exec_time
def test_function(value):
    time.sleep(5)
    print(value)

if __name__ == '__main__':
    test_function(value="super")