from utils.token import Token
from utils.enumClass import TokensTypes
from utils.C_rules import C_RESERVED_WORD
from utils.syntactic_error import Sintactic_error

class Sintax:

    def __init__(self, listToken) -> None:
        self.__tokens        = listToken
        self.__current_index = 0
        self.__current_token = listToken[0]
        self.__error_log     = Sintactic_error()
    
    #Função de movimentação nos Tokens
    def __next_token(self):
        self.__current_index += 1
        self.__current_token = self.__tokens[self.__current_index]
    
    def analyze(self):
        while(self.__current_index < len(self.__tokens)-1):
            self.__analyze_sentence()
            self.__next_token()
        self.__error_log.print()
    
    def __analyze_sentence(self):
        
        if self.__current_token.type == TokensTypes.reserved_word.value : self.__case_reserved_word()
        else: self.__error_log.add_generic_error(self.__current_token)


    def __case_reserved_word(self):
        if self.__current_token.data in C_RESERVED_WORD.directives():
            self.__case_reserved_word_directives()
        if self.__current_token.data in C_RESERVED_WORD.type_declaration():
            self.__case_reserved_word_declaration_type()
        


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
        if self.__current_token.type != TokensTypes.identifier.value:
            self.__error_log.add_unspected_type(self.__current_token, TokensTypes.identifier.value)
        self.__next_token()
        if self.__current_token.data == ';': return
        if self.__current_token.type != TokensTypes.assignment_operator.value:
            self.__error_log.add_unspected_type(self.__current_token, TokensTypes.assignment_operator.value)
        self.__equation()
    

    def __equation(self):
        self.__next_token()
        if self.__current_token.type == TokensTypes.delimiter.value: #casting
            if self.__current_token.data != '(': 
                self.__error_log.add_generic_error(self.__current_token)
                return
            self.__next_token()
            if self.__current_token.type  not in C_RESERVED_WORD.type_declaration():
                self.__error_log.add_generic_error(self.__current_token)
                return
            self.__next_token()
            if self.__current_token.data != ')': 
                self.__error_log.add_missing_final_delimiter() # rever aqui
                return
            self.__equation()
        
        if (self.__current_token.type != TokensTypes.numeric_constant.value and
            self.__current_token.type != TokensTypes.identifier.value       and
            self.__current_token.type != TokensTypes.functions.value
           ):
            self.__error_log.add_generic_error(self.__current_token)
            return
        
        self.__next_token()
        if self.__current_token.data == ';' : return
        if self.__current_token.type == TokensTypes.arithimetic_operator.value: self.__equation()


    def __case_function(self):
        pass
       