import sys
from test1.test1 import test1


if __name__ == "__main__":
    test1()
    a = sys.modules
    # print(a.keys())
    print(sys.path)