from Lexico.symbols import Symbols

class Rules:
    def __type_declaration(self): return "Declaração de tipo"
    def __include(self): return "include"
    def __return(self): return "retorno"

    
    def __analyze_token(self, token):
        symbols = Symbols()
        if token['type'] == symbols.reserved_word:
            if token['token'] in ['int', 'float', 'void', 'double', 'char']: 
                return self.__type_declaration()
            if token['token'] == '#include':
                return self.__include()
            if token['token'] == 'return':
                return self.__return()