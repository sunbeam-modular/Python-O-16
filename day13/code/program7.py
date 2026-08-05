# multiple inheritance

class Developer:
    def __init__(self, language):
        self.language = language

class Tester:
    def __init__(self, testing_type):
        self.testing_type = testing_type

class Ops:
    def __init__(self, os_administration):
        self.os_administration = os_administration

# DevOps class has mulitple parent classes
class DevOps(Developer, Tester, Ops):
    def __init__(self, language, testing_type, os_administration, tools):
        # initialize all the parent classes
        Developer.__init__(self, language=language)
        Tester.__init__(self, testing_type=testing_type)
        Ops.__init__(self, os_administration=os_administration)

        # initialize own members
        self.tools = tools

devops = DevOps('python', 'automation', 'linux', "terraform, docker, kubernetes")