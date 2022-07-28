from objects.AtributeObject import AtributeObject

class AttributeTable:
    def __init__(self):
        self.entries = []
    
    def consult(
        self,
        name,
        type,
        scope,
        insideClass,
        insideMethod
    ):
        for entry in self.entries:
            if entry.name == name and entry.type == type and entry.scope == scope and entry.insideClass == insideClass and entry.insideMethod == insideMethod:
                return entry
            else:
                return None
    
    def add(
        self,
        AtributeObject
    ):
        if self.consult(AtributeObject.name, AtributeObject.type, AtributeObject.scope, AtributeObject.insideClass, AtributeObject.insideMethod) is None:
            self.entries.append(AtributeObject)
            return True
        else:
            return False