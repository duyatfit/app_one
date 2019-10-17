from lib_one import lib_one_code
from libtwo import lib_two_code
import apache_beam as beam


def main():
    print(lib_one_code.lib_one_hello())
    print(lib_one_code.np_arange(10))
    print(lib_two_code.lib_two_hello(10))


if __name__ == "__main__":
    main()
