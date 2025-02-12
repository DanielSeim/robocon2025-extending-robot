import sys
import astpretty
from robot.api.parsing import get_model, KeywordCall, Tags, ModelVisitor, Token


model = get_model(sys.argv[1])
#astpretty.pprint(model)

class Fixer(ModelVisitor):

    def visit_TestCase(self, node):
        self.generic_visit(node)

    def visit_Tags(self, node: Tags):
        for token in node.get_tokens(Token.ARGUMENT):
            if token.value == 'bad':
                token.value = 'good'

    def visit_KeywordCall(self, node: KeywordCall):
        kw = node.get_token(Token.KEYWORD)
        if kw.value == 'Log to konsole':
            kw.value = 'Log to console'



Fixer().visit(model)
model.save('fixed.robot')