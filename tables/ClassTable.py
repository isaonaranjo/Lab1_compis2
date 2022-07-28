from objects.ClassObject import ClassObject

class ClassTable:
    def __init__(self):
        self.entries = []

    def consult(
        self,
        name,
        inheritsFrom
    ):
        for entry in self.entries:
            if entry.name == name and entry.inheritsFrom == inheritsFrom:
                return entry
            else:
                return None

    def add(
        self,
        ClassObject
    ):
        if self.consult(ClassObject.name, ClassObject.inheritsFrom) is None:
            self.entries.append(ClassObject)
            return True
        else:
            return False