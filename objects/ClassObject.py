class ClassObject:
    def __init__(
        self,
        name,
        inheritsFrom = None
    ):
        self.name = name
        self.inheritsFrom = inheritsFrom
    
    def __str__(self):
        return 'name: %s, inheritsFrom: %s' % (self.name, self.inheritsFrom)
