# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.
from tables.AllTables import *
from semanticErrors import semanticError

class FirstVisitor(ParseTreeVisitor):
    
    def __init__(self):
        super().__init__()
        self.functionTable = FunctionTable()
        self.attributeTable = AttributeTable()
        self.typesTable = TypesTable()
        self.classTable = ClassTable()
        self.currentMethod = None
        self.currentScope = 1
        self.currentClass = "Debugg"
        self.currentMethodId = 10
        self.foundErrors = []
        self.normalTypes = {"Int": 4, "Bool":4, "String": 4}
        self.currOffset = 0

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#programBlock.
    def visitProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#classDEF.
    def visitClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        className = str(ctx.TYPEID()[0])
        if len(ctx.TYPEID()) > 1:
            parentClass = str(ctx.TYPEID()[1])
            if not self.classTable.findEntry(parentClass):
                error = semanticError(ctx.start.line, "Class " + parentClass + " not defined")
                self.foundErrors.append(error)
                return "Error"
        else:
            parentClass = None
        self.currentClass = className
        self.currentMethod = None
        self.currentScope = 1
        self.currOffset = 0
        childrenResults = []
        for node in ctx.feature():
            childrenResults.append(self.visit(node))
        if parentClass:
            entry = ClassTableEntry(className, parentClass, size = sum(childrenResults) )
        else:
            entry = ClassTableEntry(className, size = sum(childrenResults))
        result = self.classTable.addEntry(entry)
        if not result:
            error = semanticError(ctx.start.line, "Class " + className + " already defined")
            self.foundErrors.append(error)
            return "Error"


    # Visit a parse tree produced by YAPLParser#MethodDef.
    def visitMethodDef(self, ctx:YAPLParser.MethodDefContext):
        self.currentMethodId += 1
        functionName = str(ctx.OBJECTID())
        type = str(ctx.TYPEID())
        entry = FunctionTableEntry(self.currentMethodId,functionName, type, self.currentScope, self.currentClass)
        result = self.functionTable.addEntry(entry)
        self.currentScope = 2
        if not result:
            error = semanticError(ctx.start.line, "Function " + functionName + " already defined")
            self.foundErrors.append(error)
            return "Error"
        else:
            self.currentMethod = functionName
            self.currOffset = 0
            for node in ctx.formal():
                self.visit(node)
            self.visit(ctx.expr())
            return 0

    # Visit a parse tree produced by YAPLParser#FeactureDecalration.
    def visitFeactureDecalration(self, ctx:YAPLParser.FeactureDecalrationContext):
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        if featureType in self.normalTypes:
            size = self.normalTypes[featureType]
        else:
            size = 4
        if self.currentMethod:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId, size = size, offset= self.currOffset)
            self.currOffset += size
        else:
            entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, None, size = size, offset= self.currOffset)
            self.currOffset += size

        result = self.attributeTable.addEntry(entry)

        if not result:
            error = semanticError(ctx.start.line, "Attribute " + featureName + " already defined")
            self.foundErrors.append(error)
            return "Error"
        else:
            self.visitChildren(ctx)
            return size


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        featureName = str(ctx.OBJECTID())
        featureType = str(ctx.TYPEID())
        if featureType in self.normalTypes:
            size = self.normalTypes[featureType]
        else:
            size = 4
        entry = AttributeTableEntry(featureName, featureType, self.currentScope, self.currentClass, self.currentMethodId, True, size= size, offset=self.currOffset)
        self.currOffset +=size
        result  = self.attributeTable.addEntry(entry)
        if not result:
            error = semanticError(ctx.start.line, "Parameter " + featureName + " already defined")
            self.foundErrors.append(error)
            return "Error"
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#newExpr.
    def visitNewExpr(self, ctx:YAPLParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#integerExpr.
    def visitIntegerExpr(self, ctx:YAPLParser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx:YAPLParser.DeclarationExpressionContext):
        return self.visitChildren(ctx)
        
    # Visit a parse tree produced by YAPLParser#ifElseExpr.
    def visitIfElseExpr(self, ctx:YAPLParser.IfElseExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#lessExpr.
    def visitLessExpr(self, ctx:YAPLParser.LessExprContext):
       return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#BraketedExpr.
    def visitBraketedExpr(self, ctx:YAPLParser.BraketedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:YAPLParser.MultiplyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letExpr.
    def visitLetExpr(self, ctx:YAPLParser.LetExprContext):
        self.currentScope += 1
        firstVisits = ctx.expr()[0:-1]
        firstVisitsResults = []
        for node in firstVisits:
            firstVisitsResults.append(self.visit(node))
        for i in range(len(ctx.OBJECTID())):
            newVarName = str(ctx.OBJECTID()[i])
            newVarType = str(ctx.TYPEID()[i])
            if newVarType in self.normalTypes:
                size1 = self.normalTypes[newVarType]
            else:
                size1 = 4
            newVarEntry = AttributeTableEntry(newVarName, newVarType, self.currentScope, self.currentClass, self.currentMethodId,size=size1, offset=self.currOffset)
            self.currOffset += size1
            result = self.attributeTable.addEntry(newVarEntry)
            if not result:
                error = semanticError(ctx.start.line, "Variable " + newVarName + " already defined")
                self.foundErrors.append(error)
                return "Error"
        self.visit(ctx.expr()[-1])
        self.currentScope -= 1
        return 0



    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx:YAPLParser.StringExprContext):
        return "String"


    # Visit a parse tree produced by YAPLParser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:YAPLParser.LessEqualExprContext):
        return self.visitChildren(ctx)
    


    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx:YAPLParser.NotExprContext):
       return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#addExpr.
    def visitAddExpr(self, ctx:YAPLParser.AddExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:YAPLParser.IsVoidExprContext):
        result = self.visit(ctx.expr())
        return "Bool"


    # Visit a parse tree produced by YAPLParser#objectIdExpr.
    def visitObjectIdExpr(self, ctx:YAPLParser.ObjectIdExprContext):
       return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#substractExpr.
    def visitSubstractExpr(self, ctx:YAPLParser.SubstractExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        return "Bool"


    # Visit a parse tree produced by YAPLParser#parenthExpr.
    def visitParenthExpr(self, ctx:YAPLParser.ParenthExprContext):
       return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        return self.visitChildren(ctx)

del YAPLParser