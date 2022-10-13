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

import tkinter as tk
from tkinter import filedialog as fd

def grafica():
    gui = tk.Tk()
    boton = tk.Frame(gui)
    codi = tk.Frame(gui)
    gui['bg'] = '#0059b3'
    boton.pack()
    codi.pack(fill = tk.X)
    gui.title("Proyecto Compiladores 2")
    usuario = tk.Text(codi)
    windowThreeAddressCode = tk.Text(codi)
    windowErrors = tk.Text(width = 100)
    compilar = tk.Button(boton, text="Compile", command=lambda: main(usuario.get("1.0", tk.END), windowErrors, windowThreeAddressCode))
    carg = tk.Button(boton, text="Load File", command=lambda: cargar(usuario))
    compilar.pack(side=tk.RIGHT, padx=15, pady=20)
    compilar.configure(font=("Comic Sans MS", 11))
    carg.pack(side=tk.LEFT, padx=15, pady=20)
    carg.configure(font=("Comic Sans MS", 11))
    usuario.pack(side=tk.LEFT,fill=tk.X)
    windowThreeAddressCode.pack(side=tk.LEFT,fill=tk.X)
    windowErrors.pack(fill=tk.Y)
    
    gui.mainloop()


def cargar(usuarioIngui):
    usuarioIngui.delete("1.0", tk.END)
    filename = fd.askopenfilename(initialdir = os.getcwd(), title = "Select a file to upload")
    with open(filename, 'r') as f:
        lines = f.read()
        usuarioIngui.insert(tk.END, lines)


def main(program, windowErrors, windowThreeAddressCode):
    windowErrors.delete("1.0", tk.END)
    windowThreeAddressCode.delete("1.0", tk.END)
    data = InputStream(program)
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

    windowErrors.insert(tk.END, stringOfErrors)

    stringOfThreeAddressCode = ''

    if (len(myYAPLNewVisitor.errors) == 0):
        threeAddressCodeVisitor = ThreeAddressCodeVisitor(myYAPLNewVisitor.table)
        threeAddressCode = threeAddressCodeVisitor.visit(tree)
        stringOfThreeAddressCode = str(threeAddressCode)
    else:
        stringOfThreeAddressCode = 'Compiler Error: Cant generate 3-address code if there are syntax errors in loaded file, please fix them and try again'

    windowThreeAddressCode.insert(tk.END,str(stringOfThreeAddressCode))

if __name__ == "__main__":
    grafica()
