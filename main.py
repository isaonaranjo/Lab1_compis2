# code extracted from -> https://faun.pub/introduction-to-antlr-python-af8a3c603d23

import sys
from tabulate import tabulate
from antlr4 import *
from antlr4.InputStream import InputStream
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from MyYAPLVisitor import MyYAPLVisitor

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = FileStream(sys.argv[1])
    else:
        data = InputStream(sys.stdin.readline())

    # lexer
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = YAPLParser(stream)
    tree = parser.program()

    # evaluator
    visitor = MyYAPLVisitor()
    visitor.visit(tree)

    print(30*"=" + " Symbols Table " + 30*"=")
    print("\n")
    print(30*"-" + " Classes " + 30*"-")
    for myClass in visitor.classTable.entries:
        print(myClass)
    print("\n")
    print(30*"-" + " Attributes " + 30*"-")
    for myAttribute in visitor.attributeTable.entries:
        print(myAttribute)
    print("\n")
    print(30*"-" + " Functions " + 30*"-")
    for myFunction in visitor.functionTable.entries:
        print(myFunction)
    print("\n")
    print(30*"=" + " End of Table " + 30*"=")