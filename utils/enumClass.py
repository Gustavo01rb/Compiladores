from enum import Enum

class TokensTypes(Enum):
    reserved_word        = "Palavra reservada"
    arithimetic_operator = "Operador aritmético"
    logic_operator       = "Operador Lógico"
    assignment_operator  = "Operador de atribuição"
    delimiter            = "Delimitador"
    library              = "Biblioteca"
    identifier           = "Identificador"
    numeric_constant     = "Constante Numérica"
    functions            = "Identificador de função"

class RegexStructure(Enum):
    reserved_word        = ["const", "while", "for", "if", "#include", "do", "return", "int", "float", "double", "char"]
    arithimetic_operator = [r'\+|-|\*|/|%', "Operador aritmético"]
    logic_operator       = [r'==|>=|<=|!=|!|<|>', "Operador Lógico"] 
    assignment_operator  = [r'=', "Operador de atribuição"]
    delimiter            = [r'\(|\)|{|}|\[|]|;', "Delimitador"]
    library              = [r'[a-z]*\.h$', "Biblioteca"]

class TokenStructure(Enum):
    type  = 'type'
    match = 'match'
    data  = 'data'