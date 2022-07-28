class FunctionObject:
    def __init__(
        self,
        name,
        type,
        parameters= None,
        scope = None,
        belongsTo = None
    ):
        self.name = name
        self.parameters = parameters
        self.scope = scope
        self.type = type
        self.belongsTo = belongsTo

    def __str__(self):
        return 'name: %s, type: %s, parameters: %s, scope: %s, belongsTo: %s' % (self.name, self.type, self.parameters, self.scope, self.belongsTo)