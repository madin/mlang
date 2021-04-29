# Generated from ../grammar/mlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\r\4\2\t\2\3\2\5\2\6\n\2\3\2\6\2\t\n\2\r\2\16\2\n\3\2")
        buf.write("\2\2\3\2\2\2\2\r\2\5\3\2\2\2\4\6\7\4\2\2\5\4\3\2\2\2\5")
        buf.write("\6\3\2\2\2\6\b\3\2\2\2\7\t\7\7\2\2\b\7\3\2\2\2\t\n\3\2")
        buf.write("\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\3\3\2\2\2\4\5\n")
        return buf.getvalue()


class mlangParser ( Parser ):

    grammarFileName = "mlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "DIV", "DIGIT" ]

    RULE_number = 0

    ruleNames =  [ "number" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    DIGIT=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(mlangParser.MINUS, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(mlangParser.DIGIT)
            else:
                return self.getToken(mlangParser.DIGIT, i)

        def getRuleIndex(self):
            return mlangParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = mlangParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mlangParser.MINUS:
                self.state = 2
                self.match(mlangParser.MINUS)


            self.state = 6 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 5
                self.match(mlangParser.DIGIT)
                self.state = 8 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mlangParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





