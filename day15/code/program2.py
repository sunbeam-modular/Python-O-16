class School:
    def __init__(self, name, address):
        self._name = name
        self._address = address

        # create empty collection of students
        self._students = []

        # index of the student info
        self._index = 0

    def enroll_student(self, name):
        self._students.append(name)

    def __str__(self):
        return f"School [name={self._name}, address={self._address}]"

    def display_students(self):
        for student in self._students:
            print(f"name = {student}")

    # make the school class iterable
    def __iter__(self):
        # reset the index to 0 so that we can start from the 0th position
        self._index = 0

        return self

    def __next__(self):
        # check if the index is within the collection's length
        if self._index >= len(self._students):
            # the index is exhausted
            raise StopIteration()
        
        # get the student at the indexth position
        student = self._students[self._index]

        # increment the index to the next position
        self._index += 1

        return student

# create a school instance
school = School("Sunbeam", "Pune")
print(school)

# enroll students
school.enroll_student("alice")
school.enroll_student("bob")
school.enroll_student("david")
school.enroll_student("john")
school.enroll_student("jane")

# get all the students from school
# school.display_students()

# get iterator object from school
# school_iterator = iter(school)
# print(f"school iterator = {school_iterator}")

# print(f"next student = {next(school_iterator)}")
# print(f"next student = {next(school_iterator)}")
# print(f"next student = {next(school_iterator)}")
# print(f"next student = {next(school_iterator)}")
# print(f"next student = {next(school_iterator)}")
# print(f"next student = {next(school_iterator)}")

# school is a collection of students
for student in school:
    print(f"student = {student}")
