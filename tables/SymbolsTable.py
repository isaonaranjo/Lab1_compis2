from objects.Class import Class
from objects.Function import Function
from objects.Attribute import Attribute

from utils.constants import INT, STRING, BOOL, VOID, OBJECT

class SymbolsTable:
    def __init__(self):
        self.classes = []
        self.functions = []
        self.attributes = []
        self.types = [INT, STRING, BOOL, VOID, OBJECT]

    def findClass(
        self,
        name
    ):
        for myClass in self.classes:
            if myClass.name == name: return myClass
            else: return None

    def addClass(
        self,
        Class
    ):
        if self.findClass(Class.name) is None:
            self.classes.append(Class)
            return True
        else: return False

    def findFunctionByName(
        self,
        name,
        belongsTo
    ):
        for myFunction in self.functions:
            if myFunction.name == name and myFunction.belongsTo == belongsTo: return myFunction
            else: return None

    def findFunctionById(
        self,
        id
    ):
        for myFunction in self.functions:
            if myFunction.id == id: return myFunction
        return None

    def addFunction(
        self,
        Function
    ):
        if self.findFunctionByName(Function.name, Function.belongsTo) is None:
            self.functions.append(Function)
            return True
        else:
            return False

    def findAttribute(
        self,
        name,
        insideClass,
        insideMethod,
        scope
    ):
        for myAttribute in self.attributes:
            if myAttribute.name == name and myAttribute.insideClass == insideClass and myAttribute.insideMethod == insideMethod and myAttribute.scope == scope:
                return myAttribute
        return None

    def findParamsOfFunction(
        self,
        functionId
    ):
        params = []
        for myAttribute in self.attributes:
            if myAttribute.insideMethod == functionId:
                if myAttribute.isParam:
                    params.append(myAttribute)
        return params

    def addAttribute(
        self,
        Attribute
    ):
        if self.findAttribute(Attribute.name, Attribute.insideClass, Attribute.insideMethod, Attribute.scope) is None:
            self.attributes.append(Attribute)
            return True
        else:
            return False

    def findType(
        self,
        type
    ):
        for myType in self.types:
            if myType == type:
                return myType
        return None

    def addType(
        self,
        type
    ):
        self.types.append(type)
