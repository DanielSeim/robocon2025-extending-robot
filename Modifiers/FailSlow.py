from robot.api import ExecutionResult, SuiteVisitor
from robot.result import TestCase
import sys


class FailSlow(SuiteVisitor):

    def __init__(self, threshold: float):
        self.threshold = threshold

    def visit_test(self, test: TestCase):
        elapsed = test.elapsed_time.total_seconds()
        if test.passed and elapsed > self.threshold:
            test.passed = False
            test.message = f'Execution time was over {self.threshold}s.'


if __name__ == '__main__':
    threshold, path = sys.argv[1:]
    result = ExecutionResult(path)
    visitor = FailSlow(float(threshold))
    result.suite.visit(visitor)
    result.save()