# Generated from ../grammar/mlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mlangParser import mlangParser
else:
    from mlangParser import mlangParser

# This class defines a complete listener for a parse tree produced by mlangParser.
class mlangListener(ParseTreeListener):

    # Enter a parse tree produced by mlangParser#number.
    def enterNumber(self, ctx:mlangParser.NumberContext):
        pass

    # Exit a parse tree produced by mlangParser#number.
    def exitNumber(self, ctx:mlangParser.NumberContext):
        pass



del mlangParser