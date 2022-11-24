from utils.predefinedTypes import *
from utils.predefinedClasses import *
from utils.predefinedFunctions import *
from utils.predefinedAttributes import *

class SymbolsTable:
    def __init__(self):
        self.classes = [IO_CLASS, OBJECT_CLASS, INT_CLASS, STRING_CLASS, BOOL_CLASS]
        self.functions = [ABORT, IN_INT, LENGTH, OUT_INT, SUBSTRING, TYPE_NAME, COPY, OUT_STRING, OUT_INT, IN_STRING, IN_INT, LENGTH, CONCAT, SUBSTRING]
        self.attributes = [OUT_STRING_ATTR, OUT_INT_ATTR, CONCAT_ATTR, SUBSTRING_START_ATTR, SUBSTRING_END_ATTR]
        self.types = [INT, STRING, BOOL, VOID, OBJECT]

    def addClass(self, Class):
        if self.findClass(Class.name) is None:
            self.classes.append(Class)
            return True
        else:
            return False

    def findClass(self, name):
        for myClass in self.classes:
            if myClass.name == name:
                return myClass
        return None

    def getFunctionWithId(self, id):
        for myFunction in self.functions:
            if myFunction.id == id:
                return myFunction
        return None

    def getFunctionWithName(self, name, isFrom):
        for myFunction in self.functions:
            if myFunction.name == name and myFunction.isFrom == isFrom:
                return myFunction
        return None

    def addFunction(self, Function):
        if self.getFunctionWithName(Function.name, Function.isFrom) is None:
            self.functions.append(Function)
            return True
        else:
            return False
    
    def AddAttribute(self, Attribute):
        if self.findAttribute(Attribute.name, Attribute.insideClass, Attribute.insideMethod, Attribute.scope) is None:
            self.attributes.append(Attribute)
            return True
        else:
            return False
    
    def findAttribute(self, name, insideClass, insideMethod, scope):
        for myAttribute in self.attributes:
            if myAttribute.name == name and myAttribute.insideClass == insideClass and myAttribute.insideMethod == insideMethod and myAttribute.scope == scope:
                return myAttribute
        return None

    def findParamsOfFunction(self, functionId):
        params = []
        for myAttribute in self.attributes:
            if myAttribute.insideMethod == functionId:
                if myAttribute.isParameterOfFunction:
                    params.append(myAttribute)
        return params

    def findNonParamsOfFunction(self, insideMethod):
        results = []
        for myAttribute in self.attributes:
            if myAttribute.insideMethod == insideMethod:
                if not myAttribute.isParameterOfFunction:
                    results.append(myAttribute)
        return results

    def addType(self, type):
        self.types.append(type)

    def findType(self, type):
        for myType in self.types:
            if myType == type:
                return myType
        return None

class AttributeTableEntry:
    def __init__(self, name, type, scope = None, inClass = None, inMethod = None, isParam = False, size = 0, offset = 0):
        self.name = name
        self.type = type
        self.scope = scope
        self.inClass = inClass
        self.inMethod = inMethod
        self.isParam = isParam
        self.size = size
        self.offset = offset
    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.name, self.type, self.scope, self.inClass, self.inMethod, self.isParam, self.size, self.offset)


class AttributeTable:
    def __init__(self, Entry = None):
        self.entries = []
        outStringEntry = AttributeTableEntry("out_string", "String",2,"IO",4,True,size=4,offset=0)
        outIntEntry = AttributeTableEntry("out_int", "Int",2,"IO",5,True, size=4, offset=0)
        concatEntry = AttributeTableEntry("concat", "String",2,"String",9,True, size=4, offset=0)
        susbstrEntry1 = AttributeTableEntry("start", "Int", 2,"String",10,True, size= 4, offset=0)
        susbstrEntry2 = AttributeTableEntry("End", "Int", 2,"String",10,True, size=4, offset=8)
        self.entries.append(outStringEntry)
        self.entries.append(outIntEntry)
        self.entries.append(concatEntry)
        self.entries.append(susbstrEntry1)
        self.entries.append(susbstrEntry2)
        if Entry:
            self.entries.append(Entry)
    
    def addEntry(self, AttributeTableEntry):
        if self.findEntry(AttributeTableEntry.name, AttributeTableEntry.inClass, AttributeTableEntry.inMethod, AttributeTableEntry.scope) is None:
            self.entries.append(AttributeTableEntry)
            return True
        else:
            return False
    
    def findEntry(self, name, inClass, inMethod, scope):
        for entry in self.entries:
            if entry.name == name and entry.inClass == inClass and entry.inMethod == inMethod and entry.scope == scope:
                return entry
        return None
    
    def findParamsOfFunction(self, functionId):
        results = []
        for entry in self.entries:
            if entry.inMethod == functionId:
                if entry.isParam:
                    results.append(entry)
        return results
    
    def findLetsOffFunction(self, inMethod):
        results = []
        for entry in self.entries:
            if entry.inMethod == inMethod:
                if not entry.isParam:
                    results.append(entry)
        return results

class ClassTableEntry:
    def __init__(self, name, inherits = "Object", size = 0):
        self.name = name
        self.inherits = inherits
        self.size = size
    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.inherits, self.size)

class ClassTable:
    def __init__(self, Entry = None):
        self.entries = []
        IOEntry = ClassTableEntry("IO", "Object")
        ObjectEntry = ClassTableEntry("Object", None)
        IntEntry = ClassTableEntry("Int", "Object")
        StringEntry = ClassTableEntry("String", "Object")
        BoolEntry = ClassTableEntry("Bool", "Object")
        self.entries.append(IOEntry)
        self.entries.append(ObjectEntry)
        self.entries.append(IntEntry)
        self.entries.append(StringEntry)
        self.entries.append(BoolEntry)
        if Entry:
            self.entries.append(Entry)

    def addEntry(self, Entry):
        if self.findEntry(Entry.name) is None:
            self.entries.append(Entry)
            return True
        else:
            return False

    def findEntry(self, name):
        for entry in self.entries:
            if entry.name == name:
                return entry
        return None


class FunctionTableEntry:
    def __init__(self,id ,name, type, scope = None,  belongsTo = None):
        self.id = id
        self.name = name
        self.type = type
        self.scope = scope
        self.belongsTo = belongsTo
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.id,self.name, self.type, self.scope, self.belongsTo)

class FunctionTable:
    def __init__(self):
        self.entries = []
        abort = FunctionTableEntry(1,"abort","Object", 1,"Object")
        type_name= FunctionTableEntry(2,"type_name","String", 1,"Object")
        copy = FunctionTableEntry(3,"copy","OBJECT", 1,"Object")
        out_string = FunctionTableEntry(4,"out_string","IO", 1,"IO")
        out_int = FunctionTableEntry(5,"out_int","IO", 1,"IO")
        in_string = FunctionTableEntry(6,"in_string","String", 1,"IO")
        in_int = FunctionTableEntry(7,"in_int","Int", 1,"IO")
        length = FunctionTableEntry(8,"length","Int", 1,"String")
        concat = FunctionTableEntry(9,"concat","String", 1,"String")
        substr = FunctionTableEntry(10,"substr","String", 1,"String")
        self.entries.append(abort)
        self.entries.append(type_name)
        self.entries.append(copy)
        self.entries.append(out_string)
        self.entries.append(out_int)
        self.entries.append(in_string)
        self.entries.append(in_int)
        self.entries.append(length)
        self.entries.append(concat)
        self.entries.append(substr)

    def addEntry(self, FunctionTableEntry):
        if self.findEntryByName(FunctionTableEntry.name, FunctionTableEntry.belongsTo) is None:
            self.entries.append(FunctionTableEntry)
            return True
        else:
            return False

    def findEntryByName(self, name, belongsTo):
        for entry in self.entries:
            if entry.name == name and entry.belongsTo == belongsTo:
                return entry                
        return None
        
    def findEntryByID(self, id):
        for entry in self.entries:
            if entry.id == id:
                return entry
        return None


class TypesTable:
    def __init__(self):
        self.entries = ["Int", "Bool", "String", "Void", "Object"]
    
    def addEntry(self, type):
        self.entries.append(type)
    
    # finds type in table
    def findEntry(self, type):
        for entry in self.entries:
            if entry == type:
                return entry
        return None