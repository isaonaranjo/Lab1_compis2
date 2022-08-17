class Function:
    def __init__(
        self,
        id,
        name,
        type,
        scope = None,
        belongsTo = None
    ):
        self.id = id
        self.name = name
        self.type = type
        self.scope = scope
        self.belongsTo = belongsTo

    def __str__(self):
        return '[FUNCTION] -> identifier: %s, type: %s, scope: %s, belongsTo: %s' % (self.name, self.type, self.scope, self.belongsTo)