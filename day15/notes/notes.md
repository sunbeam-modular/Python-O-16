# iterator and iterable

- iterable
  - the object which can be iterated is known iterable
  - the default sequence collections are iterable
    - e.g. list, tuple, set, dictionary, string
  - these objects can be iterated using a loop
  - to make a class iterable implement following methods
    - `__iter__()`: returns an object of iterator
    - `__next__()`: return next value from the collection
- iterator
  - the object which is used to iterate over an iterable
  - iter()
    - function is used to get the iterator object
    - python internally calls `__iter__()` on the object
  - next()
    - function is used on the iterator to get the next value
    - python internally calls `__next__()` on the object
    - a StopIteration exception will be raised when next() tries to go out of the collection index

# generator

- object which internally implements the iterator logic
- generator object is an iterator
- to create a generator use `yield` keyword
- used to create the values using lazy evaluation philosophy
  - unless required do not allocate the memory

# variable length argument function

- function which can accept variable number of arguments
- such function receives two parameters
  - `*args`
    - parameter to accept positional arguments
    - does not accept any keyword arguments
    - type: tuple
  - `**kwargs`
    - parameter to accept keyword arguments
    - does not accept any positional arguments
    - type: dictionary

# decorator

- a closure function which will be called before calling the actual function
- configured using @ at the of defining the function
- adding a new behavior in a function without modifying the function's code

# module

- python file with .py or .pyc extension
- used to reuse the code
- to reuse the code from another module, import the module first
- every module object has in built properties
  - `__name__`
    - name of the module
    - the name attribute has two possible values
      - `__main__`: when a module is executed
      - filename: when a module is imported
  - `__dir__`: collection of members
- importing modules
  - in python, the module can be imported anywhere in the code
  - module must be imported before using any of the entities from it
  - ways to import the modules
    - importing an entire module
      - import math_operations
      - use the module name to access the module members
    - importing an entire module with an alias
      - import math_operations as mo
      - alias is a temprary name given to the module to access the members
      - use the alias to access the module members
    - importing required entities from a module
      - from math_operations import add
      - no need to use any module name to access the members, instead use member names directly
    - importing required members with aliases
      - from math_operations import add as my_add
      - no need to use any module name to access the members, instead use the alias
- types
  - builtin modules
    - os, json, csv, time, datetime, re
  - custom modules
    - numpy, pandas, flask, pytest, beautifulsoup, matplotib
