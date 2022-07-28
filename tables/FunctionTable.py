from objects.FunctionObject import FunctionObject

class FunctionTable:
    def __init__(self):
        self.entries = []

    def consult(
        self,
        name,
        parameters,
        scope,
        type,
        belongsTo
    ):
        for entry in self.entries:
            if entry.name == name and entry.parameters == parameters and entry.scope == scope and entry.type == type and entry.belongsTo == belongsTo:
                return entry
            else:
                return None

    def add(
        self,
        FunctionObject
    ):
        if self.consult(FunctionObject.name, FunctionObject.parameters, FunctionObject.scope, FunctionObject.type, FunctionObject.belongsTo) is None:
            self.entries.append(FunctionObject)
            return True
        else:
            return False
