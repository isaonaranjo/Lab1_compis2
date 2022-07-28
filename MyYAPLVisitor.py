from YAPLParser import YAPLParser
from YAPLVisitor import YAPLVisitor

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.
from objects.ClassObject import ClassObject
from objects.AtributeObject import AtributeObject
from objects.FunctionObject import FunctionObject

from tables.ClassTable import ClassTable
from tables.AttributeTable import AttributeTable
from tables.FunctionTable import FunctionTable

CURR_CLASS = ""
CURR_METHOD = ""
CURR_SCOPE = 1

class MyYAPLVisitor(YAPLVisitor):
    def __init__(self):
        self.classTable = ClassTable()
        self.attributeTable = AttributeTable()
        self.functionTable = FunctionTable()

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
        entry = ClassObject(className)
        self.classTable.add(entry)
        CURR_CLASS = className
        CURR_SCOPE = 1
        CURR_METHOD = None
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#methodDEF.
    def visitMethodDEF(self, ctx:YAPLParser.MethodDEFContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        methodName = ctx.OBJECTID()
        methodType = ctx.TYPEID()
        entry = FunctionObject(methodName, methodType, None, CURR_SCOPE, CURR_CLASS)
        self.functionTable.add(entry)
        CURR_SCOPE = 2
        CURR_METHOD = methodName
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#featureDEF.
    def visitFeatureDEF(self, ctx:YAPLParser.FeatureDEFContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        featureName = ctx.OBJECTID()
        featureType = ctx.TYPEID()
        entry = AtributeObject(featureName, featureType, CURR_SCOPE, CURR_CLASS, CURR_METHOD)
        self.attributeTable.add(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        global CURR_CLASS, CURR_METHOD, CURR_SCOPE
        formalName = ctx.OBJECTID()
        formalType = ctx.TYPEID()
        entry = AtributeObject(formalName, formalType, CURR_SCOPE, CURR_CLASS, CURR_METHOD)
        self.attributeTable.add(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#expr.
    def visitExpr(self, ctx:YAPLParser.ExprContext):
        return self.visitChildren(ctx)


del YAPLParser