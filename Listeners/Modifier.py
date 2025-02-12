from robot.api.interfaces import ListenerV3
from robot import result, running

class Modifier(ListenerV3):
    
    def start_suite(self, data: running.TestSuite, result: result.TestSuite):
        test = data.tests.create('New!')
        test.body.create_keyword('Log', ['New...'])



    def start_user_keyword(self, 
                           data: running.Keyword, 
                           implementation: running.UserKeyword, 
                           result: result.Keyword):
        print(implementation.owner)
        implementation.body.create_keyword('Log', ['Dynamic'])


    def end_keyword(self, data: running.Keyword, result: result.Keyword):
        if result.failed and result.message == 'Something bad happened!':
            result.skipped = True
            result.message += '\nBut we do not care...'

