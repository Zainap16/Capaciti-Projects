
# Iterators and Genretors


# Iteration example 1

# for element in [1, 2, 3]:

#  print(element)

# for element in (1, 2, 3):

#  print(element)

# for key in {'one':1, 'two':2}:

#  print(key)

# for char in "123":

#  print(char)

# for line in open("./Day_2/Reflection_Week 4_Day 2.txt"):

#  print(line, end='')

# #Iteration example 2

# s = 'abc'

# it = iter(s)

# it


# next(it)

# next(it)

# next(it)

# next(it)

# File iteration example
#
# Traceback (most recent call last):

#        File "<stdin>", line 1, in <module>

#        next(it)

#        StopIteration

# Iteration example 3

import os
from math import pi, sin


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')

for char in iter(rev):
    print(char)

# Generator example 1:


def reverse(data):

    for index in range(len(data)-1, -1, -1):

        yield data[index]


for char in reverse('golf'):

    print(char)


# Generator Expressions


# sum of squares
sum_of_squares = sum(i*i for i in range(10))
print(sum_of_squares)

# dot product
xvec = [10, 20, 30]
yvec = [7, 5, 3]
dot_product = sum(x*y for x, y in zip(xvec, yvec))
print(dot_product)

# sine table
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

# unique words
page = ['This is a sentence.', 'Another sentence.']
unique_words = set(word for line in page for word in line.split())
print(unique_words)

# valedictorian


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


graduates = [Student('John', 3.8), Student('Alice', 4.0), Student('Bob', 3.9)]
valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)

# reverse data
data = 'golf'
reversed_data = list(data[i] for i in range(len(data)-1, -1, -1))
print(reversed_data)

# Operating system interface


# Returns the current working directory
print("\n--------\nReturns the current working directory:\n" +
      os.getcwd()+"\n--------\n")

print("\n--------\n")
os.chdir('./Day_1')   # Change current working directory

print("\n--------\n", os.system('mkdir today'))
# Run the command mkdir in the system shell


print("\n--------\nReturns a list of all module functions:\n",
      dir(os), "\n--------\n")
