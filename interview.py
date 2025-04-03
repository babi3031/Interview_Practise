# code-1(UST-GLOBAL)
# write a python code to print alternate vowels in given input string
# def remove_alt_vowels(string):
#     vowels="aeiouAEIOU"
#     result=""
#     count=0
#     for char in string:
#         if char in vowels:
#             if count%2==0:
#                 result+=char
#             count+=1
#         else:
#             result+=char
#     return result
#
# string=input("Enter the word:")
# print(remove_alt_vowels(string))

# code-2(UST-GLOBAL)
# covert a lait into dict
# list1=[1,2,3]
# keys=["a","b","c"]
# print(dict(zip(keys,list1)))


# numpay and pandas practise
# import numpy as np
# import pandas as pd
#
# list1=[1,2,3]
# print(np.array(list1))
# print(pd.Series(list1))


# practise for list and dict comprehnsion
# list1=[1,2,3,4]
# result=[x**2 for x in list1]
# print(result)
#
# list2=[2,3,4,5]
# result={x:x**2 for x in list2}
# print(result)
#
# lam=lambda x,y,z:(y**x)*z
# print(lam(2,5,2))
#
# practise for generators
# def squares():
#     x = range(1, 4)  # 1 to 4
#     for n in x:
#         yield n ** 2
#
#
# for y in squares():
#     print(y)

# practise for generators
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# # Creating a generator object
# fib_gen = fibonacci_generator()
#
# # Generating the first 10 Fibonacci numbers
# for _ in range(10):
#     print(next(fib_gen))

# practise for decorators
# Decorator function that takes an extra parameter
# Decorator function
# def uppercase_decorator(func):
#     # Inner function to modify the behavior of the original function
#     def wrapper(*args, **kwargs):
#         # Call the original function with the given arguments and keyword arguments
#         result = func(*args, **kwargs).upper()
#         return result
#     # Return the wrapper function
#     return wrapper
#
# # Decorate the greet function with uppercase_decorator using @ syntax
# @uppercase_decorator
# def greet(name, **kwargs):  # Accept additional keyword arguments
#     return f"Hello, {name}!" + f" your age is {kwargs.get('age')}" +f" and from {kwargs.get('city')} city" if kwargs else f"Hello, {name}!"  # Optionally include kwargs in the result
#
# # Call the decorated function
# print(greet("BabiSamineedi", age=26, city="Tuni"))  # Output: HELLO, ALICE! KWARGS: {'age': 30, 'city': 'New York'}


# import os
# print(os.path.expanduser('~'))

# import pickle
#
# # Example dictionary to pickle
# data = {'name': 'John', 'age': 30, 'city': 'New York'}
#
# # Pickling the data and storing it in a file
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)
#
# # Unpickling the data from the file
# with open('data.pickle', 'rb') as f:
#     loaded_data = pickle.load(f)
#
# # Printing the unpickled data
# print("Unpickled data:", loaded_data)

# dict={'first':'Bob', 'last':'Smith'}
# all_keys=dict.items()
# print(all_keys)
# print(type(all_keys))
# print(type(str(dict)))


#To find word frequency in given string

# def word_frequency(string):
#     words=string.split()
#     frequency = {}
#     for word in words:
#         frequency[word]=frequency.get(word,0)+1
#     return frequency
#
# string="the quick brown fox jumps over the lazy dog"
# print(word_frequency(string))
# # output : {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}



def replace_vowels(string):
    vowels = 'aeiou'
    vowel_index = 0
    result = ''
    for char in string:
        if char.lower() in vowels:
            result += vowels[vowel_index]
            vowel_index = (vowel_index + 1) % len(vowels)
        else:
            result += char
    return result

input_string = "i have a string replace now"
print("Original string:", input_string)
print("Modified string:", replace_vowels(input_string))
# output
# Original string: i have a string replace now
# Modified string: a hevi o strung rapleci now


# string = "India need 45 runs in 54 balls to win"
#
# numbers = ''.join(char if char.isdigit() else ' ' for char in string).split()
# print(numbers)
#
# sum_of_digits = 0
# for number in numbers:
#     sum_of_digits += int(number)
#
# print(sum_of_digits)
# output=99