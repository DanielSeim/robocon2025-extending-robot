from robot.api.deco import library, keyword

@library(listener='SELF')
class Library:

    def __init__(self):
        self.test = None


    def start_test(self, data, result):
        self.test = data


    @keyword
    def library_keyword(self):
        print(f'Current test is {self.test.name}')