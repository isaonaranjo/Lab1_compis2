class AtributeObject:
    def __init__(
        self,
        name,
        type,
        scope = None,
        insideClass = None,
        insideMethod = None
    ):
        self.name = name
        self.type = type
        self.scope = scope
        self.insideClass = insideClass
        self.insideMethod = insideMethod

    def __str__(self):
        return 'name: %s, type: %s, scope: %s, insideClass: %s, insideMethod: %s' % (self.name, self.type, self.scope, self.insideClass, self.insideMethod)