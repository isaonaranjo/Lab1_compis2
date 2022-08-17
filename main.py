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
    for myClass in visitor.table.classes:
        print(myClass)
    print("\n")
    for myFunction in visitor.table.attributes:
        print(myFunction)
    print("\n")
    for myAttribute in visitor.table.functions:
        print(myAttribute)
    print("\n")
    print(30*"=" + " End of Table " + 30*"=")