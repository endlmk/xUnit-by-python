
class TestCase:
    def __init__(self, name) -> None:
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    def testMethod(self):
        self.wasRun = 1
        
# test code
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
    def testSetup(self):
        self.test.run()
        assert(self.test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()

# test = WasRun("testMethod")
# print(test.wasRun)
# test.run()
# print(test.wasRun)
