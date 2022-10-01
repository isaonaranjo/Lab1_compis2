class QuadruplesStack():
    def __init__(self):
        self.quadruples = []
        self.memAddress = 't0'

    def __str__(self):
        stringQuadruples = [str(quadruple) for quadruple in self.quadruples]
        return '\n'.join(stringQuadruples)

    def addQuadruples(self, quadruples: list):
        for quadruple in quadruples: self.quadruples.append(quadruple)
        
    def changeMemAddress(self, memAddress:str): self.memAddress = memAddress
