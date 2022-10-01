# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

from objects.Quadruple import Quadruple
from objects.CodeCreator import CodeCreator
from objects.QuadruplesStack import QuadruplesStack


# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class ThreeAddressCodeVisitor(ParseTreeVisitor):
    def __init__(self, table):
        super().__init__()
        self.table = table
        self.codeCreator = CodeCreator()
        self.CLASS = None
        self.METHOD = None
        self.METHOD_NO = 10
        self.SCOPE = 1
        self.NEW_NO = 0

    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#classExpr.
    def visitClassExpr(self, ctx:YAPLParser.ClassExprContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#attribute.
    def visitAttribute(self, ctx:YAPLParser.AttributeContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        quadruplesStack = QuadruplesStack()

        temporal = self.codeCreator.createTemp()
        quadruplesStack.changeMemAddress(temporal)

        operands = [self.visit(exprNode) for exprNode in ctx.expr()]

        for operand in operands: quadruplesStack.addQuadruples(operand.quadruples)

        addQuadruple = Quadruple(
            '+',
            operands[0].memAddress,
            temporal,
            operands[1].memAddress
        )
        quadruplesStack.addQuadruples([addQuadruple])

        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#new.
    def visitNew(self, ctx:YAPLParser.NewContext):
        return self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#negation.
    def visitNegation(self, ctx:YAPLParser.NegationContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#dispatch.
    def visitDispatch(self, ctx:YAPLParser.DispatchContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#string.
    def visitString(self, ctx:YAPLParser.StringContext):
        quadruplesStack = QuadruplesStack()
        
        currentString = str(ctx.STRINGS())
        quadruplesStack.changeMemAddress(currentString)
        quadruplesStack.setType("String")

        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#assignment.
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        quadruplesStack = QuadruplesStack()

        currentBool = str(ctx.FALSE())
        quadruplesStack.changeMemAddress(currentBool)
        quadruplesStack.setType("Bool")

        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#integer.
    def visitInteger(self, ctx:YAPLParser.IntegerContext):
        quadruplesStack = QuadruplesStack()

        currentInt = str(ctx.INTEGERS())
        quadruplesStack.changeMemAddress(currentInt)
        quadruplesStack.setType("Int")
        
        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#parenthesis.
    def visitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#not.
    def visitNot(self, ctx:YAPLParser.NotContext):
        self.visit(ctx.program())

    # Visit a parse tree produced by YAPLParser#isVoid.
    def visitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        self.visit(ctx.program())

    # Visit a parse tree produced by YAPLParser#function.
    def visitFunction(self, ctx:YAPLParser.FunctionContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#bracket.
    def visitBracket(self, ctx:YAPLParser.BracketContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        quadruplesStack = QuadruplesStack()

        currentBool = str(ctx.TRUE())
        quadruplesStack.changeMemAddress(currentBool)
        quadruplesStack.setType("Bool")

        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#let.
    def visitLet(self, ctx:YAPLParser.LetContext):
        self.visit(ctx.program())

    # Visit a parse tree produced by YAPLParser#divide.
    def visitDivide(self, ctx:YAPLParser.DivideContext):
        quadruplesStack = QuadruplesStack()

        temporal = self.codeCreator.createTemp()
        quadruplesStack.changeMemAddress(temporal)

        operands = [self.visit(exprNode) for exprNode in ctx.expr()]

        for operand in operands: quadruplesStack.addQuadruples(operand.quadruples)

        divideQuadruple = Quadruple(
            '/',
            operands[0].memAddress,
            temporal,
            operands[1].memAddress
        )

        quadruplesStack.addQuadruples([divideQuadruple])
        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        self.visit(ctx.program())

    # Visit a parse tree produced by YAPLParser#lessEqual.
    def visitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        self.visit(ctx.program())


    # Visit a parse tree produced by YAPLParser#multiply.
    def visitMultiply(self, ctx:YAPLParser.MultiplyContext):
        quadruplesStack = QuadruplesStack()

        temporal = self.codeCreator.createTemp()
        quadruplesStack.changeMemAddress(temporal)

        operands = [self.visit(exprNode) for exprNode in ctx.expr()]

        for operand in operands: quadruplesStack.addQuadruples(operand.quadruples)

        multiplyQuadruple = Quadruple(
            '*',
            operands[0].memAddress,
            temporal,
            operands[1].memAddress
        )

        quadruplesStack.addQuadruples([multiplyQuadruple])
        return quadruplesStack


    # Visit a parse tree produced by YAPLParser#ifElse.
    def visitIfElse(self, ctx:YAPLParser.IfElseContext):
        self.visit(ctx.program())

    # Visit a parse tree produced by YAPLParser#substract.
    def visitSubstract(self, ctx:YAPLParser.SubstractContext):
        quadruplesStack = QuadruplesStack()

        temporal = self.codeCreator.createTemp()
        quadruplesStack.changeMemAddress(temporal)

        operands = [self.visit(exprNode) for exprNode in ctx.expr()]

        for operand in operands: quadruplesStack.addQuadruples(operand.quadruples)

        substractQuadruple = Quadruple(
            '-',
            operands[0].memAddress,
            temporal,
            operands[1].memAddress
        )

        quadruplesStack.addQuadruples([substractQuadruple])
        return quadruplesStack



del YAPLParser