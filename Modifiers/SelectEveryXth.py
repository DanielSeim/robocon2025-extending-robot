from robot.api import SuiteVisitor
from robot.running import TestSuite, TestCase

class SelectEveryXth(SuiteVisitor):

    def __init__(self, x: int = 2, start: int = 0):
        self.x = x
        self.start = start


    def start_suite(self, suite:TestSuite):
        suite.tests = suite.tests[self.start::self.x]


    def start_test(self, test: TestCase):
        group = test.body.create_group('New group')
        group.body.create_keyword('Log', ['Hello!'])
        group.body.create_keyword('Log', ['Hi, again!'])