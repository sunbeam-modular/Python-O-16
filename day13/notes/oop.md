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
