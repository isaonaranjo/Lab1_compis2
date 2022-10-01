class CodeCreator():
    def __init__(self):
        self.tempControl = 0
    
    def createTemp(self):
        self.tempControl +=1
        return f't{self.tempControl}'