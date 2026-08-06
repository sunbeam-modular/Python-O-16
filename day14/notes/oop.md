# Object oriented programming

- paradigm to use objects (created using classes) to oraganize the code
- the classes will bind the data and operations together

## class

- template or blueprint to create an object
- used to bring the data (set of attributes) and member function (methods) togther
- use class keyword to create a class in python
- members
  - every class has two types of members
    - data members: attributes or properties to store the values/data
    - member functions: methods, used to peform operation(s) on the class attributes
  - accessing the members
    - unlike other languages like Java, Python does NOT provide any keyword, rather in python we follow conventions
    - public members
      - the memebers which can accessed outside the class (using object reference)
      - convention: use no underscore at the time of declaring the member, will make the member public
      - e.g. self.name = "person1" -> will make the name attribute public
      - risk: since these members are accessible outside the class, anyone can update them with invalid values
    - protected members
      - the members which can be accessible within the same class and all the child classes
      - though python allows the protected members to be accessible outside the class, conventionally this should be programmed
      - convetion: in python, use single underscore `(_)` prefix to make a member protected
    - private members
      - the members which can be accessible only within the class
      - the members which can not be accessed outside the class and any of the child classes
      - convention: in python, use double underscore `(__)` prefix to make a member private
- data members
  - attributes stored along with the keys
  - types
    - class attributes/properties
      - by default, shared among all the instances of class
      - every object will get the same value of these members
      - but if an object updates the value of these members, a copy of it gets created/added to the object
      - access these member using class name instead of using object reference
    - instance attributes/properties
      - these members are stored inside the individual objects
      - every object will store a copy of these members
- member functions
  - also known as methods
  - types
    - class method
      - used to access the class properties
    - instance method
      - used to access the instance properties
      - every instance method must accept the first parameter which is an object of the same class
      - most often the first parameter of these methods is `self`
      - self
        - reference to the object of same class
        - similar to `this` in C++ or Java
        - is NOT a keyword
        - is a conventionally used parameter name
        - since it is a parameter of instance method(s), it can be used only inside the instance methods
      - types
        - initializer
          - a special method of a class which is used to initialize the class members
          - in python the method must use name as `__init__()`
          - gets called implicitly/automatically for every object when an object gets constructed (to initialize it)
          - similar to constructor in Java or C++
          - every class in python, must have a initializer method
            - if an explicit initializer is not added by developer, compiler adds one implicitly
          - default initializer: initializer method which does not accept any parameter
          - custom initializer: initializer method which accepts at least one parameter
          - does not return anything
        - de-initilizer
          - special method of class which is used to deallocate the members of an object accumulated in its lifecycle
          - name of de-initilizer = `__del__`
          - similar to destructor in C++
          - gets called implicitly / automatically for every object just before the object gets destroyed from memory
          - this method is not responsible for deleting the object
          - this method gets called just before the object gets destroyed from memory
          - this methods allows
            - close connections
            - close files
            - persist the data
        - setter or mutator
          - used to set value of an attribute
          - mostly it is used for private members
        - getter or inspector
          - used to get current value of an attribute
          - mostly it is used for private members
        - facilitator
          - method which adds a facility in the class

### types

- empty class: the class which does not any body except pass keyword

## object

- instance of a class
- python does not require new keyword to create an object from a class
- object always gets created in the heap area
- the reference will be created on stack
- every object has a unique memory address
  - every object may store unique data

### characteristics

- identifier
  - every object has a unique identifier (memory address)
- state
  - every object has a state which is the values stored in that object

## conventions

- in python the methods start and end with double-underscore are referred as `dunder methods`
  - dunder = d(double) under(underscore)
  - `__init__()` => dunder init
- access specifiers
  - no underscore prefix: public
  - single underscore prefix: protected
  - double underscore prefix: private

## code reuse

### association

- when two classes (objects) are externally associated
- types
  - composition
    - the relationship between two classes is strong
    - is also known as composed-of relationship
    - e.g. Car is composed-of Engine, Room is composed-of Wall
  - aggregation
    - the relationship between two classes is weak
    - is also known as has-a relationship
    - e.g. Employee has-a laptop, Person has-a car

### inheritance

- creating one class using another class
- also known as is-a relationship
- one class inherits the details with class
- terminologies
  - parent class
    - also known as base class or super class
    - from where the members will get inherited in child class
  - child class
    - also known as derived class or subclass
    - where the members from parent class will get inherited
- rule of thumb
  - child class object always contains an object of parent class
    - scenario1: child class does not contain any explicit initializer
      - the compiler automatically adds initializer in the child class
      - and creates or initializes a parent class object inside child class object
    - scenario2: child class has explicit initializer
      - child class must initialize an object of parent class explicitly
  - the child will inherit the public and protected members
  - the child will NOT be able to access the private members of parent class
- types
  - single inheritance
    - simple inheritance where there is only one parent class and one child class
    - e.g. Employee is derived from Person class
  - multi-level inheritance
    - child class acts as a base class for another chlid class
    - e.g. Manager is derived from Employee, Employee is derived from Person class
      - Person is parent class of Employee and grand-parent of Manager
      - Manager is a child class of Employee and grand-child of Person
  - mulitple inehritance
    - a child class has more than one parent class
    - e.g. DevOps Engineer is a developer, tester as well as Ops person
  - hierarchical inheritance
    - a base class has more than one child classes
    - e.g. Employee is-a Person, Player is-a Person, Student is-a Person
  - hybrid inheritance
    - combination of two or more inheritances
    - e.g. Employee is-a Person, Player is-a Person, Manager is-a Employee
- note:
  - all the public and protected members from parent class are inherited to child class
    - since the child class always contains an object of parent class
    - the child class can access all the public and protected members of parent class
  - the parent class can NOT access any members of child class
- root class
  - since python3, all the classes in python are derived from `object` class
  - the `object` class is a built in class known as a root class

    ```python

      # object is the base class of Person
      class Person:
        pass

      # object is the base class of Car
      class Car():
        pass

      # object is the base class of Animal
      class Animal(object):
        pass

    ```

  - the object (root) class has the common methods which are required for all the classes
    - all methods required to manage the memory
    - string representation method

## polymorphism

- types
  - compile time polymorphism
    - also known as function overloading
    - multiple functions having same name but
      - different type of arguments
        ```c++
        - function1(int num, char *name)
        - function1(float salary)
        ```
      - different order of arguments
        ```c++
        - function1(int num, char *name)
        - function1(char *name, int num)
        ```
      - different number of arguments
        ```c++
        - function1(int num)
        - function1(char *name, float salary)
        ```
    - is not supported in python

  - run time polymorphism
    - also known as method overriding
    - a parent class method implementation is not suffient for the child class
    - a child can implement a method with same name as that of the parent class
    - method gets called from type of object
    - built-in methods
      - `__str__()`
        - returns the string representation of an object
        - by default it is implemented by object class to return default format
      - `__init__()`
        - used to initialize the method
        - by default implemented by object class to do nothing

## operator overloading (using magical methods)

- giving different meaning to the default operators
- the basic operators can work with different data types
- mathematical operators
  - rule: return the result in the form an object of custom class
  - addition: `__add__`
  - subtraction: `__sub__`
  - multiplication: `__mul__`
  - true division: `__truediv__`
  - floor division: `__floordiv__`
  - mod: `__mod__`
- comparison operators
  - rule: always returns boolean result
    - `==`: `__eq__`
    - `!=`: `__ne__`
    - `>`: `__gt__`
    - `<`: `__lt__`
    - `>=`: `__ge__`
    - `<=`: `__le__`

## exception handling

- exception
  - runtime error which by default crashes the application
  - in python all exceptions are dervied from Exception class
- Exception
  - is the base class for all exceptions in python
- exception handling
  - handling the exception to avoid the application crash
  - keywords
    - try
      - block used to add the code which may raise an error at runtime
      - every try block must be associated with at least one except block
    - except
      - always attached with a try block
      - block used to handle the exception
      - will be executed only when application raises an error
      - in case if there is no exception raised, the exception block will never execute
      - types
        - specific except block
          - this except block gets executed only when the specified exception is raised
          - a try block may be associated with one more more specific except blocks
          - syntax: `except <Exception class name>`
        - generic except block
          - this except block gets called for any type of exception
          - only one generic block is allowed for a try block
          - must appear at the end of the except blocks
    - else
      - optionally used to execute the code in case of no exception
      - mainly it is used to make the code more readables
      - will be executed only when there is no exception raised
      - it always comes after except block
      - only one else block can be associated with a try block
    - finally
      - optionally used to execute the code irrespective of exception
      - only one finally block is allowed for a try block
      - e.g. closing a file, closing connection
    - raise
      - used to raise an exception of type Exception or Custom exception class
