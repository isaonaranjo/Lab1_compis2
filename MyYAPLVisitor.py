from YAPLParser import YAPLParser
from YAPLVisitor import YAPLVisitor

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.
from objects.Class import Class
from objects.Attribute import Attribute
from objects.Function import Function

from tables.SymbolsTable import SymbolsTable

CURR_CLASS = ""
CURR_METHOD = ""
CURR_SCOPE = 1
CURR_ID = 1000

class MyYAPLVisitor(YAPLVisitor):
    def __init__(self):
        self.table = SymbolsTable()

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#programBlock.
    def visitProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classDEF.
    def visitClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        className = ctx.TYPEID()[0]
        entry = Class(className)
        self.table.addClass(entry)
        CURR_CLASS = className
        CURR_SCOPE = 1
        CURR_METHOD = None
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#methodDEF.
    def visitMethodDEF(self, ctx:YAPLParser.MethodDEFContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        methodName = ctx.OBJECTID()
        methodType = ctx.TYPEID()
        entry = Function(CURR_ID, methodName, methodType, CURR_SCOPE, CURR_CLASS)
        self.table.addFunction(entry)
        CURR_SCOPE = 2
        CURR_METHOD = methodName
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#featureDEF.
    def visitFeatureDEF(self, ctx:YAPLParser.FeatureDEFContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        featureName = ctx.OBJECTID()
        featureType = ctx.TYPEID()
        entry = Attribute(featureName, featureType, CURR_SCOPE, CURR_CLASS, CURR_METHOD)
        self.table.addAttribute(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        formalName = ctx.OBJECTID()
        formalType = ctx.TYPEID()
        entry = Attribute(formalName, formalType, CURR_SCOPE, CURR_CLASS, CURR_METHOD)
        self.table.addAttribute(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#expr.
    def visitExpr(self, ctx:YAPLParser.ExprContext):
        return self.visitChildren(ctx)


del YAPLParser