import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    a = book_to_words()
    b = len(a[0])
    for i in range(len(a)):
        if len(a[i]) > b:
            b = len(a[i])
    for i in range(len(a)):
        a[i] += '\0'.encode('ascii', 'replace') * (b - len(a[i]))
    for i in range(b - 1, -1, -1):
        a = counting_sort(a, i)
    for i in range(len(a)):
        a[i] = a[i].decode('ascii').replace('\x00', '')
        a[i] = bytes(a[i], encoding='ascii')
    return a

def count_sort_letters(array, size, col, base):
    output   = [0] * size
    count    = [0] * base
    min_base = ord('@')

    for item in array:
        correct_index = min(len(item) - 1, col)
        letter = ord(item[-(correct_index + 1)]) - min_base
        count[letter] += 1

    for i in range(base - 1):
        count[i + 1] += count[i]

    for i in range(size - 1, -1, -1):
        item = array[i]
        correct_index = min(len(item) - 1, col)
        letter = ord(item[-(correct_index + 1)]) - min_base
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output

def radix_sort_letters(array):
    size = len(array)

    max_col = len(max(array, key = len))

    for col in range(max_col):
        array = count_sort_letters(array, size, col, 26)

    return array
