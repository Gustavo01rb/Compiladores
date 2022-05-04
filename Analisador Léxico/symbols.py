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
    def end_line(self):
        return "Fim de linha"

    #Funções de verficação
    def get_reserved_word_list(self):
        return ["const", "while", "for", "if", "#include", "stdio.h", "stdlib.h", "do", "return", "int", "string", "float", "double", "bool"]
    def get_arithimetic_operator(self):
        return r'\+|-|\*|/|%'
    def get_logic_operator(self):
        return r'==|>=|<=|!=|!|<|>'
    def get_assignment_operator(self):
        return r'='
    def get_delimiter(self):
        return r'\(|\)|{|}|\[|]'
    def get_end_line(self):
        return r';$'
    

    #Funções de resposta
    def is_reserved_word(self, key):
        if key in self.get_reserved_word_list():
            return {
                "type": self.reserved_word
                }
        return False
    
    def is_arithimetic_operator(self, key):
        if re.findall(self.get_arithimetic_operator(), key):
            return {
                "type" : self.arithimetic_operator,
                "match": re.findall(self.get_arithimetic_operator(), key)
                }
        return False
    
    def is_logic_operator(self, key):
        if re.findall(self.get_logic_operator(), key):
            return {
                "type"  : self.logic_operator,
                "match" : re.findall(self.get_logic_operator(), key)
            }
        return False
        
    def is_assignment_operator(self, key):
        if re.findall(self.get_assignment_operator(), key):
            return {
                "type" : self.assignment_operator,
                "match": re.findall(self.get_assignment_operator(), key)
            }
        return False

    def is_delimiter(self, key):
        if re.findall(self.get_delimiter(), key):
            return {
                "type" : self.delimiter,
                "match": re.findall(self.get_delimiter(), key)
            }
        return False

    def is_end_of_line(self, key):
        if re.findall(self.get_end_line(), key):
            return {
                "type" : self.end_line,
                "match": re.findall(self.get_end_line(), key)
            }
        return False


    