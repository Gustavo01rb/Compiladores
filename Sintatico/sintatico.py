from urllib import response
from Lexico.symbols import Symbols

class Sintatico:
    def __type_declaration(self): return "Declaração de tipo"
    def __include(self): return "include"
    def __return(self): return "retorno"

    def __type_declaration_way(self): 
        return [self.__symbols.delimiter, self.__symbols.library, self.__symbols.delimiter]
    def __include_way(self): 
        return [self.__symbols.delimiter, self.__symbols.library, self.__symbols.delimiter]
    def __return_way(self):  
        return [self.__symbols.identifier, self.__symbols.numeric_constant]



    def __init__(self, tokens) -> None:
        self.__symbols = Symbols()
        self.__tokens = tokens


    def __analyze_token(self, token):
        symbols = Symbols()
        if token['type'] != symbols.reserved_word:
            return token['type']
        if token['token'] in ['int', 'float', 'void', 'double', 'char']: 
            return self.__type_declaration()
        if token['token'] == '#include':
            return self.__include()
        if token['token'] == 'return':
            return self.__return()

    def __analyze_expression(self, index, response_type):
        index += 1
        if response_type == self.__include():
            for iterator in self.__include_way():
                if self.__tokens[index]['type'] == iterator:
                    index += 1
                    continue
                print("Erro sintático, linha {}.\nUm {} era esperado.".format(self.__tokens[index]['line'], iterator))
                return -1
        return index


    def analyze(self, index = 0):
        symbols = Symbols()
        while index < len(self.__tokens):
            iterator = self.__tokens[index]
            response = self.__analyze_expression(index, self.__analyze_token(iterator))
            if response == -1: return
            index += response
            
            

            

            
            