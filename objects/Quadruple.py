# code extracted from https://github.com/GabrielBMiranda/MiniJava_Compiler/blob/6e56fc290375adb3ac1812570a1e4b3f0522cff4/IR_PAI/UnaryAssignmentIR.py

class Quadruple():
    def __init__(
        self, 
        operator, 
        arg1, 
        result, 
        arg2 = None
    ):
        self.operator = operator
        self.arg1 = arg1
        self.result = result
        self.arg2 = arg2
    
    def __str__(self):
        if self.operator == "=" : return f'{self.result} {self.operator} {self.arg1}'
        if self.arg2 != None: return f'{self.result} = {self.arg1} {self.operator} {self.arg2}'
        else: return f'{self.result} = {self.operator}{self.arg1}'
