from utils.token import Token
from utils.enumClass import TokenStructure, TokensTypes
from utils.C_rules import C_RESERVED_WORD
from errors.syntactic_error import Sintactic_error

class Sintax:

    def __init__(self, listToken, file_name) -> None:
        self.__tokens        = listToken
        self.__current_index = 0
        self.__current_token = listToken[0]
        self.__error_log     = Sintactic_error(file_name)
    
    #Função de movimentação nos Tokens
    def __next_token(self): 
        self.__current_index += 1
        if self.__current_index >= len(self.__tokens)-1:
            self.__current_token = self.__tokens[-1]
            return
        self.__current_token = self.__tokens[self.__current_index]
    
    def analyze(self, print=False):
        while(self.__current_index < len(self.__tokens)):
            self.__analyze_sentence()
            self.__next_token()
        if(print): self.__error_log.print()
    
    def __analyze_sentence(self):
        
        if self.__current_token.type == TokensTypes.reserved_word.value : self.__case_reserved_word()
        if self.__current_token.type == TokensTypes.identifier.value : self.__case_identifier()

    def __case_identifier(self):
        self.__next_token()
        if self.__current_token.type == TokensTypes.assignment_operator.value: 
            self.__equation()
            return
        if self.__current_token.type == TokensTypes.arithimetic_operator.value:
            if self.__current_token.data != '++' and self.__current_token.data != '--':
                self.__error_log.add_generic_error(self.__current_token)
                return
            return 
        else:
            self.__error_log.add_generic_error(self.__current_token)
            

    def __case_reserved_word(self):
        if self.__current_token.data in C_RESERVED_WORD.directives():
            self.__case_reserved_word_directives()
        if self.__current_token.data in C_RESERVED_WORD.type_declaration():
            self.__case_reserved_word_declaration_type()
        if self.__current_token.data in C_RESERVED_WORD.returns():
            self.__case_reserved_word_returns()
        if self.__current_token.data in C_RESERVED_WORD.functions():
            self.__case_reserved_word_functions()

    def __case_reserved_word_returns(self):
        self.__equation()

    def __case_reserved_word_functions(self):    
        if self.__current_token.data == "for" : self.__case_reserved_word_functions_for() 
    
    def __case_reserved_word_functions_for(self):
        self.__next_token()
        if self.__current_token.data != "(":
            self.__error_log.add_unspected_token(self.__current_token, "(", TokensTypes.delimiter.value)
        self.__next_token()
        if self.__current_token.type == TokensTypes.identifier.value: pass
        elif  self.__current_token.data in C_RESERVED_WORD.type_declaration(): self.__next_token()
        else: self.__error_log.add_generic_error(self.__current_token)
        self.__next_token()
        if self.__current_token.type != TokensTypes.assignment_operator.value:
            self.__error_log.add_unspected_token(self.__current_token, "=", TokensTypes.assignment_operator.value)
        self.__next_token()
        if self.__current_token.type != TokensTypes.numeric_constant.value:
            self.__error_log.add_unspected_token(self.__current_token, "=", TokensTypes.assignment_operator.value)
        self.__next_token()
        if self.__current_token.data != ";":
            self.__error_log.add_unspected_token(self.__current_token, ";", TokensTypes.delimiter.value)
        self.__next_token()
        if self.__current_token.type != TokensTypes.identifier.value:
            self.__error_log.add_unspected_token(self.__current_token, "Nome de variável", TokensTypes.identifier.value)
        self.__next_token()
        if self.__current_token.type != TokensTypes.logic_operator.value:
            self.__error_log.add_unspected_token(self.__current_token, "", TokensTypes.logic_operator.value)
        self.__next_token()
        if self.__current_token.type != TokensTypes.numeric_constant.value:
            self.__error_log.add_unspected_token(self.__current_token, "=", TokensTypes.assignment_operator.value)
        self.__next_token()
        if self.__current_token.data != ";":
            self.__error_log.add_unspected_token(self.__current_token, ";", TokensTypes.delimiter.value)      

    def __case_reserved_word_directives(self):
        if self.__current_token.data == "#include": 
            self.__next_token()
            if self.__current_token.data != '<': 
                self.__error_log.add_unspected_token(self.__current_token, '<', TokensTypes.delimiter.value)

            self.__next_token()
            if self.__current_token.type != TokensTypes.library.value: 
                self.__error_log.add_unspected_token(self.__current_token, '.h', TokensTypes.library.value)
                
            self.__next_token()
            if self.__current_token.data != '>': 
                self.__error_log.add_unspected_token(self.__current_token, '>', TokensTypes.delimiter.value)
    
    def __case_reserved_word_declaration_type(self):
        self.__next_token()
        if self.__case_reserved_word_declaration_type_identifier(): return
        if self.__current_token.type == TokensTypes.functions.value:
            self.__case_function()
            return
        else: self.__error_log.add_unspected_type(self.__current_token, TokensTypes.identifier.value)
    
    def __case_reserved_word_declaration_type_identifier(self):
        if self.__current_token.type != TokensTypes.identifier.value: return False
        self.__next_token()
        if self.__current_token.type == TokensTypes.separator.value:
            self.__next_token()
            return self.__case_reserved_word_declaration_type_identifier()
            
        if self.__current_token.data == ';': return True
        if self.__current_token.type != TokensTypes.assignment_operator.value:
            self.__error_log.add_unspected_type(self.__current_token, TokensTypes.assignment_operator.value)
        self.__equation()
        if self.__current_token.type == TokensTypes.separator.value:
            self.__next_token()
            return self.__case_reserved_word_declaration_type_identifier()
        if self.__current_token.data == ';': return True
        
        return True

    def __equation(self, next = True):
        if next: self.__next_token()
        if self.__current_token.type == TokensTypes.delimiter.value: #casting
            if self.__current_token.data != '(': 
                self.__error_log.add_generic_error(self.__current_token)
                return
            self.__next_token()
            if (self.__current_token.type == TokensTypes.numeric_constant.value or
                self.__current_token.type == TokensTypes.identifier.value       or
                self.__current_token.type == TokensTypes.functions.value):
                self.__equation(False)

            elif self.__current_token.type  not in C_RESERVED_WORD.type_declaration():
                self.__error_log.add_generic_error(self.__current_token)
                return
            if self.__current_token.data != ')':
                self.__error_log.add_missing_final_delimiter() # rever aqui
                return
            else: return

        if  self.__current_token.type == TokensTypes.txt.value or self.__current_token.type == TokensTypes.character.value : return
        
        if (self.__current_token.type != TokensTypes.numeric_constant.value and
            self.__current_token.type != TokensTypes.identifier.value       and
            self.__current_token.type != TokensTypes.functions.value):
            self.__error_log.add_generic_error(self.__current_token)
            return
        
        self.__next_token()
        if    self.__current_token.type == TokensTypes.arithimetic_operator.value: self.__equation()
        elif  self.__current_token.data == ';' : return
        elif  self.__current_token.data == ',' : return
        elif  self.__current_token.type == TokensTypes.delimiter.value: return
        else: self.__error_log.add_missing_final_delimiter(self.__current_token)


    def __case_function(self):
        self.__next_token()
        if self.__current_token.data != '(':
            self.__error_log.add_unspected_token(self.__current_token, '(', TokensTypes.delimiter.value)
        self.__next_token()
        if self.__current_token.data != ')':
            self.analyze()
            if self.__current_token.data != ')':
                self.__error_log.add_unspected_token(self.__current_token, ')', TokensTypes.delimiter.value)
        self.__next_token()
        if self.__current_token.data != '{':
            self.__error_log.add_unspected_token(self.__current_token, '{', TokensTypes.delimiter.value)
        self.__next_token()
        if self.__current_token.data != '}':
            self.analyze()
            if self.__current_token.data != '}':
                self.__error_log.add_unspected_token(self.__current_token, '}', TokensTypes.delimiter.value)