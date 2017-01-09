from __future__ import print_function
import sys
import atexit
import time
def function():
    i = 1
    while i<10:
        print (i)
        sys.stdout.flush()
        time.sleep(1.0)
        i +=1


def atexit_function():
    print("atexit called")
    sys.exit(0)


if __name__ == "__main__":
    atexit.register(atexit_function)
    function()
