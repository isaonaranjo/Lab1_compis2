class Class:
    def __init__(
        self,
        name,
        inheritsFrom = None
    ):
        self.name = name
        self.inheritsFrom = inheritsFrom
    
    def __str__(self):
        return '[CLASS] -> Identifier: %s, inheritsFrom: %s' % (self.name, self.inheritsFrom)
