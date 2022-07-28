# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#programBlock.
    def visitProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classDEF.
    def visitClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#feature.
    def visitFeature(self, ctx:YAPLParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#expr.
    def visitExpr(self, ctx:YAPLParser.ExprContext):
        return self.visitChildren(ctx)



del YAPLParser