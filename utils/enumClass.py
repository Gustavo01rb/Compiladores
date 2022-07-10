from enum import Enum
from utils.C_rules import C_RESERVED_WORD

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
    separator            = "Separador"
    txt                  = "Texto"
    character            = "Caractere"

class RegexStructure(Enum):
    reserved_word        = C_RESERVED_WORD.all()
    assignment_operator  = [r'=|\+=|-=', TokensTypes.assignment_operator.value]
    txt                  = [r'^".*"$', TokensTypes.txt.value]
    separator            = [r',', TokensTypes.separator.value]
    character            = [r'^\'\w+\'$', TokensTypes.character.value]
    library              = [r'\w+\.h$', TokensTypes.library.value]
    arithimetic_operator = [r'\+\+|--|\+|-|\*|/', TokensTypes.arithimetic_operator.value]
    logic_operator       = [r'==|>=|<=|!=|!|<|>', TokensTypes.logic_operator.value] 
    delimiter            = [r'\(|\)|{|}|\[|]|;', TokensTypes.delimiter.value]


class TokenStructure(Enum):
    type  = 'type'
    match = 'match'
    data  = 'data'

class DeclaredType(Enum):
    integer  = "Inteiro"
    floating = "Flutuante"
    string   = "String"
    char     = "Caractere"

class RegexTypes(Enum):
    integer  = [r'^\d+$', DeclaredType.integer.value]
    floating = [r'^\d+\.\d+$|^\d+$', DeclaredType.floating.value]
    string   = [r'^"\w+|\s*"$', DeclaredType.string.value]
    char     = [r'^\'\w{1}\'$', DeclaredType.char.value]