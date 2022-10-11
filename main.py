import sys
import os
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from YAPLVisitor import YAPLVisitor
from antlr4.tree.Trees import Trees
from MyYAPLVisitor import MyYAPLVisitor
from MyYAPLNewVisitor import MyYAPLNewVisitor
from ThreeAddressCodeVisitor import ThreeAddressCodeVisitor
from objects.Error import Error

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = FileStream(sys.argv[1])
    else:
        data = InputStream(sys.stdin.readline())

    #lexer
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    #parser
    parser = YAPLParser(stream)
    tree = parser.program()

    # evaluator
    myYAPLVisitor = MyYAPLVisitor()
    myYAPLVisitor.visit(tree)

    myYAPLNewVisitor = MyYAPLNewVisitor(myYAPLVisitor.table, myYAPLVisitor.errors)
    myYAPLNewVisitor.visit(tree)
    
    stringOfErrors = myYAPLNewVisitor.buildErrorString()

    stringOfThreeAddressCode = ''
    if (len(myYAPLNewVisitor.errors) == 0):
        threeAddressCodeVisitor = ThreeAddressCodeVisitor(myYAPLNewVisitor.table)
        threeAddressCode = threeAddressCodeVisitor.visit(tree)
        stringOfThreeAddressCode = str(threeAddressCode)
    else:
        stringOfThreeAddressCode = 'Compiler Error: Cant generate 3-address code if there are syntax errors in loaded file, please fix them and try again'

    print(stringOfErrors)
    print(stringOfThreeAddressCode)
