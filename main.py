# code extracted from -> https://faun.pub/introduction-to-antlr-python-af8a3c603d23

import sys
import os
from antlr4 import *
from antlr4.InputStream import InputStream
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from YAPLVisitor import YAPLVisitor

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
    
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)
    #evaluator
    visitor = YAPLVisitor()
    output = visitor.visit(tree)
    print(output)