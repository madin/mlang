# Generated from ../grammar/mlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4\7\5\t")
        buf.write("\6\13\7\3\2\2\2\26\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2\7\21")
        buf.write("\3\2\2\2\t\23\3\2\2\2\13\25\3\2\2\2\r\16\7-\2\2\16\4\3")
        buf.write("\2\2\2\17\20\7/\2\2\20\6\3\2\2\2\21\22\7,\2\2\22\b\3\2")
        buf.write("\2\2\23\24\7\61\2\2\24\n\3\2\2\2\25\26\4\62;\2\26\f\3")
        buf.write("\2\2\2\3\2\2")
        return buf.getvalue()


class mlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    DIGIT = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "TIMES", "DIV", "DIGIT" ]

    ruleNames = [ "PLUS", "MINUS", "TIMES", "DIV", "DIGIT" ]

    grammarFileName = "mlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


