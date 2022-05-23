import re

class Symbols:
    #Definindo as constantes
    @property
    def reserved_word(self):
        return "Palavra reservada"
    @property
    def arithimetic_operator(self):
        return "Operador aritmético"
    @property
    def logic_operator(self):
        return "Operador Lógico"
    @property
    def assignment_operator(self):
        return "Operador de atribuição"
    @property
    def delimiter(self):
        return "Delimitador"
    @property
    def library(self):
        return "Biblioteca"
    @property
    def identifier(self):
        return "Identificador"
    @property
    def numeric_constant(self):
        return "Constante Numérica"
    @property
    def function(self):
        return "Identificador de função"

    #Funções de verficação
    def __get_reserved_word_list(self):
        return ["const", "while", "for", "if", "#include", "stdio.h", "stdlib.h", "do", "return", "int", "float", "double"]
    def __get_arithimetic_operator(self):
        return r'\+|-|\*|/|%'
    def __get_logic_operator(self):
        return r'==|>=|<=|!=|!|<|>'
    def __get_assignment_operator(self):
        return r'='
    def __get_delimiter(self):
        return r'\(|\)|{|}|\[|]|;'
    def __get_library(self):
        return r'\.h$'


    

    #Funções de resposta
    def is_reserved_word(self, key):
        if key in self.__get_reserved_word_list():
            return {
                "type": self.reserved_word
                }
        return False
    
    def is_arithimetic_operator(self, key):
        if re.findall(self.__get_arithimetic_operator(), key):
            return {
                "type" : self.arithimetic_operator,
                "match": re.findall(self.__get_arithimetic_operator(), key)
                }
        return False
    
    def is_logic_operator(self, key):
        if re.findall(self.__get_logic_operator(), key):
            return {
                "type"  : self.logic_operator,
                "match" : re.findall(self.__get_logic_operator(), key)
            }
        return False
        
    def is_assignment_operator(self, key):
        if re.findall(self.__get_assignment_operator(), key):
            return {
                "type" : self.assignment_operator,
                "match": re.findall(self.__get_assignment_operator(), key)
            }
        return False

    def is_delimiter(self, key):
        if re.findall(self.__get_delimiter(), key):
            return {
                "type" : self.delimiter,
                "match": re.findall(self.__get_delimiter(), key)
            }
        return False
    
    def is_library(self, key):
        return re.search(self.__get_library(), key)
        



    