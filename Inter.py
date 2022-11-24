from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.
from InterCode.struc import *

class IntermediateCodeGenerator(ParseTreeVisitor):
    
    def __init__(self, classTable, functionTable, attributeTable, typesTable):
        super().__init__()
        self.functionTable = functionTable
        self.attributeTable = attributeTable
        self.typesTable = typesTable
        self.classTable = classTable
        self.temporalGenerator = TemporalGenerator()
        self.labelGenerator = LableGenerator()
        self.currentClass = None
        self.currentMethodId = 10
        self.currentScope = 1
        self.currentMethod = None
        self.newCounter = 0

    # Visit a parse tree produced by YAPL2Parser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        result = self.visit(ctx.programBlock())
        return result


    # Visit a parse tree produced by YAPL2Parser#programBlock.
    def visitProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        productionInfo = ProductionInformation()
        if not ctx.EOF():
            classdefResult = self.visit(ctx.classDEF())
            programBlockResult = self.visit(ctx.programBlock())
            productionInfo.addCode(classdefResult.code)
            productionInfo.addCode(programBlockResult.code)
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#classDEF.
    def visitClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        className = str(ctx.TYPEID()[0])
        self.currentClass = className
        self.currentMethod = None
        self.currentScope = 1
        productionInfo = ProductionInformation()
        productionInfo.addCode([Quadruple('label',"innit{0}".format(className),None)])
        
        for node in ctx.feature():
            result = self.visit(node)
            productionInfo.addCode(result.code)
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#MethodDef.
    def visitMethodDef(self, ctx:YAPLParser.MethodDefContext):
        self.temporalGenerator.resetTemporalCount()
        productionInfo = ProductionInformation()
        functionName = str(ctx.OBJECTID())
        self.currentMethodId += 1
        self.currentScope = 2
        childResult = self.visit(ctx.expr())
        productionInfo.addCode([Quadruple("label","{0}{1}".format(functionName, self.currentClass),None)])
        productionInfo.addCode(childResult.code)
        productionInfo.addCode([Quadruple("=",childResult.addr, "functionCallReturnAddr")])
        #print(productionInfo)
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#FeactureDecalration.
    def visitFeactureDecalration(self, ctx:YAPLParser.FeactureDecalrationContext):
        productionInfo = ProductionInformation()
        assignTo = str(ctx.OBJECTID())
        assignToEntry = self.attributeTable.findEntry(assignTo, self.currentClass, None,self.currentScope)
        if ctx.expr():
            result = self.visit(ctx.expr())
            productionInfo.addCode(result.code)
            codeToAdd = Quadruple("=",result.addr,"OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))
            productionInfo.addCode([codeToAdd])
        else:
            if assignToEntry.type == "Int":
                codeToAdd = Quadruple("=",0,"OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))
            elif assignToEntry.type == "Bool":
                codeToAdd = Quadruple("=",0,"OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))  
            elif assignToEntry.type == "String":
                codeToAdd = Quadruple("=",'',"OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))  
            else:
                pass
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#newExpr.
    def visitNewExpr(self, ctx:YAPLParser.NewExprContext):
        productionInfo = ProductionInformation()
        newInstance = str(ctx.TYPEID())
        classEntry = self.classTable.findEntry(newInstance)
        productionInfo.setAddr("Object_{0}{1}".format(newInstance, self.newCounter))
        productionInfo.addCode([Quadruple("allocate_in_heap", classEntry.size, None )])
        productionInfo.type = newInstance
        self.newCounter +=1
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#divideExpr.
    def visitDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        productionInfo = ProductionInformation()
        address = self.temporalGenerator.newTemporal()
        productionInfo.setAddr(address)
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
            productionInfo.addCode(result.code)
        productionCode = Quadruple('/',childrenResults[0].addr, address ,childrenResults[1].addr )
        productionInfo.addCode([productionCode])
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        productionInfo = ProductionInformation()
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        #Find the entry of the function in current class
        methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), self.currentClass)
        #Search it in parent class
        if not methodEntry:
            usingClass = self.classTable.findEntry(self.currentClass)
            methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), usingClass.inherits)
        savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
        letDefinitions = self.attributeTable.findLetsOffFunction(methodEntry.id)
        size = 0
        for i in savedParams:
            size += i.size
        for j in letDefinitions:
            size += j.size
        productionInfo.addCode([Quadruple("allocate_in_stack", size, None)])
        for i in range(len(childrenResults)):
            if i < len(savedParams):
                productionInfo.addCode(childrenResults[i].code)
                productionInfo.addCode([Quadruple("=",childrenResults[i].addr,"Function_{0}{1}[{2}]".format(methodEntry.name,methodEntry.belongsTo,savedParams[i].offset))])
        productionInfo.addCode([Quadruple("call","{}{}".format(methodEntry.name, methodEntry.belongsTo), None)])
        productionInfo.addr = "functionCallReturnAddr"
        productionInfo.type = methodEntry.type
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#integerExpr.
    def visitIntegerExpr(self, ctx:YAPLParser.IntegerExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(str(ctx.INTEGERS()))
        productionInfo.type = "Int"
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(str(ctx.TRUE()))
        productionInfo.type ="Bool"
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        productionInfo = ProductionInformation()
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode(childrenResults[0].code)
        #Find the entry of the function in current class
        if ctx.TYPEID():
            methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), str(ctx.TYPEID()))
        else:
            mainClass = childrenResults[0].type
            methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), mainClass) 
            if not methodEntry:
                parentClass = self.classTable.findEntry(self.currentClass).inherits
                methodEntry = self.functionTable.findEntryByName(str(ctx.OBJECTID()), parentClass)
        productionInfo.type = methodEntry.type
        savedParams = self.attributeTable.findParamsOfFunction(methodEntry.id)
        letDefinitions = self.attributeTable.findLetsOffFunction(methodEntry.id)
        size = 0
        for i in savedParams:
            size += i.size
        for j in letDefinitions:
            size += j.size
        params = childrenResults[1:]
        productionInfo.addCode([Quadruple("allocate_in_stack", size, None)])
        for i in range(len(params)):
            if i < len(savedParams):
                productionInfo.addCode(params[i].code)
                productionInfo.addCode([Quadruple("=",params[i].addr,"Function_{0}{1}[{2}]".format(methodEntry.name,methodEntry.belongsTo,savedParams[i].offset))])
        productionInfo.addCode([Quadruple("call","{}{}".format(methodEntry.name, methodEntry.belongsTo), None)])
        productionInfo.setAddr("functionCallReturnAddr")
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx:YAPLParser.DeclarationExpressionContext):
        productionInfo = ProductionInformation()
        assignTo = str(ctx.OBJECTID())
        assignToEntry = self.attributeTable.findEntry(assignTo, self.currentClass, self.currentMethodId,self.currentScope)
        scope = self.currentScope  
        while scope  > 0:
            if assignToEntry is None:
                assignToEntry = self.attributeTable.findEntry(assignTo, self.currentClass, self.currentMethodId ,scope)
            if assignToEntry is None:
                assignToEntry = self.attributeTable.findEntry(assignTo, self.currentClass, None ,scope)
            scope -= 1
        childrenResult = self.visit(ctx.expr())
        productionInfo.addCode(childrenResult.code)
        if assignToEntry.inMethod:
            methodEntry = self.functionTable.findEntryByID(assignToEntry.inMethod)
            codeToAdd = Quadruple("=",childrenResult.addr,"Function_{0}{1}[{2}]".format(methodEntry.name,assignToEntry.inClass, assignToEntry.offset))
            productionInfo.setAddr("Function_{0}{1}[{2}]".format(methodEntry.name,assignToEntry.inClass, assignToEntry.offset))
            
        else:
            codeToAdd = Quadruple("=",childrenResult.addr,"OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))
            productionInfo.setAddr("OBJECT_{0}[{1}]".format(assignToEntry.inClass, assignToEntry.offset))
        productionInfo.addCode([codeToAdd])
        if len(childrenResult.addr) == 2 and "t" in childrenResult.addr:
            self.temporalGenerator.freeTemporal(childrenResult.addr)
        return productionInfo
        
    # Visit a parse tree produced by YAPL2Parser#ifElseExpr.
    def visitIfElseExpr(self, ctx:YAPLParser.IfElseExprContext):
        productionInfo = ProductionInformation()
        next = self.labelGenerator.generateNext()
        booleanTrue, booleanFalse = self.labelGenerator.generateIfLabels()
        ctx.inheritedAttributes = (next, booleanTrue, booleanFalse)
        returnAddr = self.temporalGenerator.newTemporal()
        childrenResults = []
        productionInfo.next = next
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode(childrenResults[0].code)
        if childrenResults[0].code[-1].opp != "goto":
            productionInfo.addCode([Quadruple("eq",childrenResults[0].addr, booleanTrue, 1)])
            productionInfo.addCode([Quadruple("goto", booleanFalse, None)]) 
        productionInfo.addCode([Quadruple("label",booleanTrue,None)])
        productionInfo.addCode(childrenResults[1].code)
        productionInfo.addCode([Quadruple("=",childrenResults[1].addr,returnAddr)])
        productionInfo.addCode([Quadruple("goto",next,None)])
        productionInfo.addCode([Quadruple("label",booleanFalse, None)])
        productionInfo.addCode(childrenResults[2].code)
        productionInfo.addCode([Quadruple("=",childrenResults[2].addr,returnAddr)])
        productionInfo.addCode([Quadruple("label", next, None)])
        productionInfo.setAddr(returnAddr)
        if len(childrenResults[1].addr) == 2 and "t" in childrenResults[1].addr:
                self.temporalGenerator.freeTemporal(childrenResults[1].addr)
        if len(childrenResults[2].addr) == 2 and "t" in childrenResults[2].addr:
                self.temporalGenerator.freeTemporal(childrenResults[2].addr)
        #print(productionInfo)
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#lessExpr.
    def visitLessExpr(self, ctx:YAPLParser.LessExprContext):
        productionInfo = ProductionInformation()
        inheritedAtributes = ctx.parentCtx.inheritedAttributes
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode(childrenResults[0].code)
        productionInfo.addCode(childrenResults[1].code)
        productionInfo.addCode([Quadruple("<",childrenResults[0].addr, inheritedAtributes[1], childrenResults[1].addr)])
        productionInfo.addCode([Quadruple("goto", inheritedAtributes[2], None)])
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#BraketedExpr.
    def visitBraketedExpr(self, ctx:YAPLParser.BraketedExprContext):
        productionInfo = ProductionInformation()
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
            productionInfo.addCode(result.code)
        productionInfo.addr = childrenResults[-1].addr
        #print(productionInfo)
        
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:YAPLParser.MultiplyExprContext):
        productionInfo = ProductionInformation()
        address = self.temporalGenerator.newTemporal()
        productionInfo.setAddr(address)
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
            productionInfo.addCode(result.code)
        productionCode = Quadruple('*',childrenResults[0].addr, address ,childrenResults[1].addr )
        if len(childrenResults[0].addr) == 2 and "t" in childrenResults[0].addr:
            self.temporalGenerator.freeTemporal(childrenResults[0].addr)
        if len(childrenResults[1].addr) == 2 and "t" in childrenResults[1].addr:
            self.temporalGenerator.freeTemporal(childrenResults[1].addr)
        productionInfo.addCode([productionCode])
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#letExpr.
    def visitLetExpr(self, ctx:YAPLParser.LetExprContext):
        productionInfo = ProductionInformation()
        self.currentScope += 1
        firstVisits = ctx.expr()[0:-1]
        firstVisitsResutls = []
        for node in firstVisits:
            firstVisitsResutls.append(self.visit(node))
        for i in range(len(ctx.OBJECTID())):
            if i < len(ctx.ASIGNOPP()):
                name = str(ctx.OBJECTID()[i])
                varEntry = self.attributeTable.findEntry(name, self.currentClass, self.currentMethodId, self.currentScope)
                productionInfo.addCode(firstVisitsResutls[i].code)
                if varEntry.inClass:
                    productionInfo.addCode([Quadruple("=",firstVisitsResutls[i].addr, "Function_{0}{1}[{2}]".format(self.currentMethod,varEntry.inClass, varEntry.offset))])
                else:
                    productionInfo.addCode([Quadruple("=",firstVisitsResutls[i].addr, "Object_{}[{}]".format(varEntry.inClass, varEntry.offset))])
        lastChild = self.visit(ctx.expr()[-1])
        productionInfo.addCode(lastChild.code)
        productionInfo.setAddr(lastChild.addr)
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#stringExpr.
    def visitStringExpr(self, ctx:YAPLParser.StringExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(str(ctx.STRINGS()))
        productionInfo.type = "String"
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:YAPLParser.LessEqualExprContext):
        productionInfo = ProductionInformation()
        inheritedAtributes = ctx.parentCtx.inheritedAttributes
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode(childrenResults[0].code)
        productionInfo.addCode(childrenResults[1].code)
        productionInfo.addCode([Quadruple("<=",childrenResults[0].addr, inheritedAtributes[1], childrenResults[1].addr)])
        productionInfo.addCode([Quadruple("goto", inheritedAtributes[2], None)])
        return productionInfo
    
    # Visit a parse tree produced by YAPL2Parser#notExpr.
    def visitNotExpr(self, ctx:YAPLParser.NotExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(self.temporalGenerator.newTemporal())
        chidlrenResult = self.visit(ctx.expr())
        productionInfo.addCode(chidlrenResult.code)
        productionInfo.addCode([Quadruple("!=",chidlrenResult.addr, productionInfo.addr)])
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#whileExpr.
    def visitWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        productionInfo = ProductionInformation()
        trueLabel, falseLabel, begin = self.labelGenerator.generateWhileLables()
        ctx.inheritedAttributes = (begin, trueLabel, falseLabel)
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode([Quadruple("label",begin,None)])
        productionInfo.addCode(childrenResults[0].code)
        print(len(childrenResults[0].code))
        if len(childrenResults[0].code) == 0 or childrenResults[0].code[-1].opp != "goto":
            productionInfo.addCode([Quadruple("eq",childrenResults[0].addr,trueLabel,1)])
            productionInfo.addCode([Quadruple("goto",falseLabel,None)])
        productionInfo.addCode([Quadruple("label",trueLabel,None)])
        productionInfo.addCode(childrenResults[1].code)
        productionInfo.addCode([Quadruple("goto",begin,None)])
        productionInfo.addCode([Quadruple("label",falseLabel,None)])
        productionInfo.setAddr(childrenResults[1].addr)
        #print(productionInfo)
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#addExpr.
    def visitAddExpr(self, ctx:YAPLParser.AddExprContext):
        productionInfo = ProductionInformation()
        address = self.temporalGenerator.newTemporal()
        productionInfo.setAddr(address)
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
            productionInfo.addCode(result.code)
        productionCode = Quadruple('+',childrenResults[0].addr, address ,childrenResults[1].addr )
        productionInfo.addCode([productionCode])
        if len(childrenResults[0].addr) == 2 and "t" in childrenResults[0].addr:
            self.temporalGenerator.freeTemporal(childrenResults[0].addr)
        if len(childrenResults[1].addr) == 2 and "t" in childrenResults[1].addr:
            self.temporalGenerator.freeTemporal(childrenResults[1].addr)
       
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:YAPLParser.IsVoidExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(self.temporalGenerator.newTemporal())
        chidlrenResult = self.visit(ctx.expr())
        productionInfo.addCode(chidlrenResult.code)
        productionInfo.addCode([Quadruple("void",chidlrenResult.addr, productionInfo.addr)])
        productionInfo.type = "Bool"
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#objectIdExpr.
    def visitObjectIdExpr(self, ctx:YAPLParser.ObjectIdExprContext):
        varName = str(ctx.OBJECTID())
        varEntry = self.attributeTable.findEntry(varName, self.currentClass, self.currentMethodId,self.currentScope)
        scope = self.currentScope 
        while scope  > 0:
            if varEntry is None:
                varEntry = self.attributeTable.findEntry(varName, self.currentClass, self.currentMethodId ,scope)
            if varEntry is None:
                varEntry = self.attributeTable.findEntry(varName, self.currentClass, None ,scope)
            if varEntry is not None:
                break
            scope -= 1
        productionInfo = ProductionInformation()
        if varName == "self":
            productionInfo.setAddr("this")
            return productionInfo
        if varEntry.inMethod:
            methodEntry = self.functionTable.findEntryByID(varEntry.inMethod)
            productionInfo.setAddr("Function_{0}{1}[{2}]".format(methodEntry.name,varEntry.inClass, varEntry.offset))
        else:
            productionInfo.setAddr("OBJECT_{0}[{1}]".format(varEntry.inClass, varEntry.offset))
        productionInfo.type = varEntry.type
        return productionInfo

    # Visit a parse tree produced by YAPL2Parser#substractExpr.
    def visitSubstractExpr(self, ctx:YAPLParser.SubstractExprContext):
        productionInfo = ProductionInformation()
        address = self.temporalGenerator.newTemporal()
        productionInfo.setAddr(address)
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
            productionInfo.addCode(result.code)
        productionCode = Quadruple('-',childrenResults[0].addr, address ,childrenResults[1].addr )
        productionInfo.addCode([productionCode])
        if len(childrenResults[0].addr) == 2 and "t" in childrenResults[0].addr:
            self.temporalGenerator.freeTemporal(childrenResults[0].addr)
        if len(childrenResults[1].addr) == 2 and "t" in childrenResults[1].addr:
            self.temporalGenerator.freeTemporal(childrenResults[1].addr)        
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#falseExpr.
    def visitFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        productionInfo = ProductionInformation()
        productionInfo.setAddr(str(ctx.FALSE()))
        productionInfo.type = "Bool"
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#parenthExpr.
    def visitParenthExpr(self, ctx:YAPLParser.ParenthExprContext):
        productionInfo = self.visit(ctx.expr())
        return productionInfo


    # Visit a parse tree produced by YAPL2Parser#equalExpr.
    def visitEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        productionInfo = ProductionInformation()
        inheritedAtributes = ctx.parentCtx.inheritedAttributes
        childrenResults = []
        for node in ctx.expr():
            result = self.visit(node)
            childrenResults.append(result)
        productionInfo.addCode(childrenResults[0].code)
        productionInfo.addCode(childrenResults[1].code)
        productionInfo.addCode([Quadruple("eq",childrenResults[0].addr, inheritedAtributes[1], childrenResults[1].addr)])
        productionInfo.addCode([Quadruple("goto", inheritedAtributes[2], None)])
        return productionInfo 

del YAPLParser