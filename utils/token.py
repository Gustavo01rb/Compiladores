from utils.enumClass import DeclaredType

class Token:
    def __init__(self,data, type, line):
        self.data = data
        self.type = type
        self.line = line
    
    def add_declared_type(self, declared):
        if declared == "int" : 
            self.declared_type = DeclaredType.integer.value
            return
        if declared == "float" :
            self.declared_type = DeclaredType.floating.value
            return 