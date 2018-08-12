import sys

from numbers_to_text import number_to_words

if __name__ == '__main__':
    if len(sys.argv) > 1:
        number = sys.argv[1]
        print(number_to_words(number))