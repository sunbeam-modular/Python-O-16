class Employee:
    def __init__(self, name, address, email):
        self._name = name
        self._address = address
        self._email = email

    def __str__(self):
        return f"| {self._name:<10} | {self._address:<10} | {self._email:<25} |"

class Company:
    def __init__(self, name, address):
        self._name = name
        self._address = address

        # create empty collection for every employee
        self._employees = []

        # maintain the index
        self._index = 0

    def recruit_employee(self, name, address, email):
        # create an employee object
        employee = Employee(name, address, email)

        # add the employee to the collection
        self._employees.append(employee)

    def __iter__(self):
        # reset the index position
        self._index = 0
        return self

    def __next__(self):
        # check if the index is within the range
        if self._index >= len(self._employees):
            raise StopIteration()

        # get the employee at the indexth position
        employee = self._employees[self._index]

        # increment the index position
        self._index += 1

        # return the employee object
        return employee

# create company object
company = Company(name="Sunbeam", address="Pune")

# recruit employees
company.recruit_employee("amit", "pune", "amit@sunbeaminfo.com")
company.recruit_employee("nilesh", "pune", "nilesh@sunbeaminfo.com")
company.recruit_employee("rahul", "pune", "rahulk@sunbeaminfo.com")
company.recruit_employee("rahul", "karad", "rahuls@sunbeaminfo.com")

# company as collection of employees
for employee in company:
    print(employee)