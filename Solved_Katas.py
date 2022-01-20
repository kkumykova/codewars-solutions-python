# orm The Minimum - 7Kyu

def min_value(digits):
    return int("".join(map(str, sorted(set(digits)))))

print(min_value([1, 3, 1]))


# Testing 1-2-3 - 7Kyu

def number(lines):
    numbered_lines = []
    for n, text in enumerate(lines):
        numbered_lines.append(str(n + 1) + ": " + text)

    return numbered_lines


print(number(["a", "b", "c"]))


# Lost number in number sequence - 7Kyu


def find_deleted_number(arr, mixed_arr):
    if len(arr) != len(mixed_arr):
        print(set(arr))
        print(set(mixed_arr))
        num_dif = list(set(arr) - set(mixed_arr))

        return int("".join(str(e) for e in num_dif))
    else:
        return 0


print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))


# Combine objects - 7Kyu
def combine(*args):
    comb = {}
    for i in args:
        for k, v in i.items():
            if k in comb:
                comb[k] += v
            else:
                comb[k] = v
    return comb


print(combine({'a': 10, 'b': 20, 'c': 30}, {'a': 3, 'c': 6, 'd': 3}))

"""
The items() method returns a view object. The view object contains the k-v pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary.
"""


# Sum without highest and lowest number - 8Kyu

def sum_array(arr):
    sorted_arr = []
    sum_res = []

    if not arr:
        return 0

    elif arr:
        sorted_arr = sorted(arr)

        if len(sorted_arr) > 1:
            sum_res = sorted_arr[1:-1]
            return sum(sum_res)
        elif len(sorted_arr) == 1:
            return 0

    else:
        return 0


print(sum_array([6, 2, 1, 8, 10]))


# Difference of Volumes of Cuboids - 8kYU

def find_difference(a, b):
    x = a[0] * a[1] * a[2]
    y = b[0] * b[1] * b[2]
    return max(x, y) - min(x, y)


print(find_difference([2, 2, 3], [5, 4, 1]))


# 16+18=214 7Kyu

def add(num1, num2):
    odd_one = []
    sum_nums = []

    one = [int(i) for i in str(num1)]
    two = [int(i) for i in str(num2)]

    if len(one) < len(two):
        len_dif = int(len(two) - len(one))
        d = two[:len_dif]
        temp_list = two[len_dif:]
        sum_nums += [sum(pair) for pair in zip(temp_list, one)]
        string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints

    elif len(one) > len(two):
        len_dif = int(len(one) - len(two))
        d = one[:len_dif]
        temp_list = one[len_dif:]
        sum_nums += [sum(pair) for pair in zip(temp_list, two)]
        string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints
    else:
        sum_nums += [sum(pair) for pair in zip(one, two)]
        string_ints = [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints


print(add(122, 81))


# Is it a palindrome? - 8Kyu
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


print(is_palindrome('AAAAAAAAAAAAAAAAAAAAAAA'))


# Is it even? - 8Kyu
def is_even(n):
    return (n % 2) == 0


# Area or Perimeter - 8Kyu
"""You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter."""


def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return l * 2 + w * 2


print(area_or_perimeter(3, 3))


# Baby shark lyrics generator - 7Kyu
# Create a function, as short as possible, that returns baby shark lyrics.


def baby_shark_lyrics():
    d = ' doo' * 6
    prs = ['Baby ', 'Mommy ', 'Daddy ', 'Grandma ', 'Grandpa ']
    s = ""
    for p in prs:
        s += (p + 'shark,' + d + '\n') * 3 + (p + 'shark!\n')
    return s + ("Let's go hunt," + d + '\n') * 3 + ("Let's go hunt!\n") + "Run away,…"


print(baby_shark_lyrics())

# Slice the middle of a list backwards - 7Kyu
"""Write a function that takes a list of at least four elements as an argument and
returns a list of the middle two or three elements in reverse order."""


def reverse_middle(lst):
    middle = int(len(lst) / 2)
    nr_of_int_to_return = len(lst) - middle

    non_reverse_list = lst[middle - 1:nr_of_int_to_return + 1]

    reversed_list = non_reverse_list[::-1]

    return reversed_list


print("Reverse middle solution", reverse_middle([1, 2, 3, 4, 5]))

# Remove the minimum - 7Kyu
"""Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a low"""


def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        first_occurrence_of_min = numbers.index(min(numbers))
        return numbers[:first_occurrence_of_min] + numbers[first_occurrence_of_min + 1:]


print(remove_smallest([1, 2, 3, 1, 1]))

# Sum the Repeats - 7Kyu
# sum up all numbers that appear in two or more lists in the input list


"""The standard library provides the Python defaultdict type - a dictionary-like clas
behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key,
then defaultdict will automatically create the key and generate a default value for it.
This makes defaultdict a valuable option for handling missing keys in dictionaries."""

from collections import defaultdict


def repeat_sum(l):
    count = defaultdict(int)

    for l1 in l:
        for val in set(l1):
            count[val] += 1

    return sum(k for k, v in count.items() if v > 1)


print("The sum is", repeat_sum([[1, 2], [2, 4], [3, 4, 4, 4], [123456789]]))


# Sum of a nested list - 7Kyu
def sum_nested(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):  # checks if `i` is a list
            total += sum_nested(i)
        else:
            total += i
    return total


print("The sum of this nested list is:", sum_nested([1, [1], [[1]], [[[1]]]]))


# Duplicate sandwich - 7Kyu
def duplicate_sandwich(arr):
    start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
    print(start)
    print(end)
    return arr[start + 1:end]


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))


# String cleaning - 8Kyu
def string_clean(s):
    return ''.join([i for i in s if not i.isdigit()])


print(string_clean('E3at m2e2!'))


# repeatIt - 8Kyu

# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string"
def repeat_it(string, n):
    return string * n if type(string) == str else 'Not a string'


print(repeat_it("*-*", 5))


# Alternative solution using isinstance function which returns True if the specified object is of the specified type,
# otherwise False:

def repeat_it(string, n):
    return string * n if isinstance(string, str) else 'Not a string'


print(repeat_it("*^*", 5))
from collections import defaultdict


def repeat_sum(l):
    count = defaultdict(int)
    for l1 in l:
        for val in set(l1):
            count[val] += 1

    return sum(k for k, v in count.items() if v > 1)


#  Capitalization and Mutability - 8Kyu
# fix the function below:
# def capitalize_word(word):
#     return "".join(char.upper() for char in word)

def capitalize_word(word):
    return word.capitalize()


capitalize_word('word')


#  Disorganised page lists - 7Kyu

#  return an array with numbers that are out of place

def find_page_number(pages):
    n, miss = 1, []  # set n to 1 and an empty array miss for misplaced numbers

    for i in pages:
        if i != n:
            miss.append(i)
        else:
            n += 1
    return miss


print(find_page_number([1, 2, 10, 3, 4, 5, 8, 6, 7]))


#  Map over a list of lists - 7Kyu
#  Write a function which maps a function over the lists in a list

def grid_map(lst, op):  # which performs op(element) for all elements of lst
    return [[*map(op, x)] for x in lst]


# A List Comprehension follows the basic pattern:
# [ <do something to item>  for  <item> in <list>]

char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
print(grid_map(char_grid, lambda x: x.upper()))


# Dictionary from two lists - 7Kyu

#  1. return a dict from a list of keys and a list of values
#  2. if there are not enough values, the keys for these values should be None
#  3. if there are not enough keys, these values should be ignored.

def createDict(keys, values):
    if len(keys) > len(values):
        values += (len(keys) - len(values)) * [None]
        #  zip(keys, values)  # get pairs of elements
        #  dict(zip(keys, values))  # convert to dictionary
    return dict(zip(keys, values))  # return dictionary


print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(createDict(['a', 'b', 'c'], [1, 2, 3, 4]))


# Isograms - 7Kyu
def is_isogram(string):
    unique_len = len(set(string.lower()))
    if unique_len < len(string):
        return False
    else:
        return True


print("Is this string an isogram? ", is_isogram('aba'))
print("Is this string an isogram? ", is_isogram('Dermatoglyphics'))


# Unique Sum - 7Kyu
def unique_sum(lst):
    return sum(set(lst)) if lst else None


print("The unique sum of the numbers in a given list is: ", unique_sum([2, 3, 3, 3]))


# Max diff - easy - 7Kyu
def max_diff(lst):
    if len(lst) != 0:
        return max(lst) - min(lst)
    else:
        return 0


print("The difference is", max_diff([1, 2, 3, -4]))
