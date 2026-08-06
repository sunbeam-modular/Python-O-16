class Developer:
    def __init__(self, name, language):
        self._name = name
        self._language = language

    def display(self):
        print(f"called from Developer class")
        print(f"name         = {self._name}")
        print(f"language     = {self._language}")
        print('-' * 80)

class Tester():
    def __init__(self, name, testing_type):
        self._name = name
        self._testing_type = testing_type

    def display(self):
        print(f"called from Tester class")
        print(f"name         = {self._name}")
        print(f"testing type = {self._testing_type}")
        print('-' * 80)

class DevOps(Developer, Tester):
    def __init__(self, name, language, testing_type, tools):
        Developer.__init__(self, name, language)
        Tester.__init__(self, name, testing_type)
        self._tools = tools

class DevOpsClone(Developer, Tester):
    def __init__(self, name, language, testing_type, tools):
        Developer.__init__(self, name, language)
        Tester.__init__(self, name, testing_type)
        self._tools = tools

    def display(self):
        print("called from DevOpsClone class")
        print(f"name         = {self._name}")
        print(f"language     = {self._language}")
        print(f"testing type = {self._testing_type}")
        print('-' * 80)


# create an object of Developer class
developer = Developer("developer1", "c++")

# this method will be called from Developer class
developer.display()


# create an object of DevOps class
devops = DevOps("devops engineer1", "python", "automation", "terraform, docker, kubernetes")

# since the DevOps class does not implement the display(),
# following statement will call display() from the Developer class
# since the Developer class is the first one the Parent class declaration sequence
devops.display()


# create an object of DevOpsClone class
devops_clone = DevOpsClone("devops engineer1", "python", "automation", "terraform, docker, kubernetes")

# since DevOpsClone class has overriden the display(), 
# the following statement will call display() from DevOpsClone class
devops_clone.display()

# print the base classes of each of the class
print(f"base class of DevOps class      = {DevOps.__bases__}")
print(f"base class of DevOpsClone class = {DevOpsClone.__bases__}")
print(f"base class of Developer class   = {Developer.__base__}")
print(f"base class of Tester class      = {Tester.__base__}")

