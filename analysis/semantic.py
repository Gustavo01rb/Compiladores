from utils.token import Token
from utils.types import Types
from utils.C_rules import C_RESERVED_WORD
from utils.enumClass import TokensTypes
from errors.semantic_error import Semantic_error
from utils.enumClass import DeclaredType

class Semantic:
    
    def __init__(self, listToken) -> None:
        self.__tokens        = listToken
        self.__current_index = 0
        self.__current_token = listToken[0]
        self.__scope = list()
        self.__error_log = Semantic_error()
    
    def __next_token(self): 
        self.__current_index += 1
        if self.__current_index >= len(self.__tokens)-1:
            self.__current_token = self.__tokens[-1]
            return
        self.__current_token = self.__tokens[self.__current_index]

    def __find_valid_token(self):
        while( self.__current_token.type != TokensTypes.numeric_constant.value and 
               self.__current_token.type != TokensTypes.functions.value        and
               self.__current_token.type != TokensTypes.identifier.value       and
               self.__current_token.data != ";"): self.__next_token()
    
    def __add_token(self, scope = list()):
        if not scope: pass
        elif Types.is_list(scope[-1]):
            self.__add_token(scope[-1])
            return
        scope.append(self.__current_token)

    def analyze(self):
        while(self.__current_index < len(self.__tokens)):
            self.__analyze_token()
            self.__next_token()
        self.__error_log.print()
    
    def __analyze_token(self):
        if self.__current_token.data == "{":
            self.__create_new_scope(self.__scope)
        elif self.__current_token.data in C_RESERVED_WORD.type_declaration():
            self.__add_variable()
    
    def __create_new_scope(self, List):
        if not List: return
        if Types.is_list(List[-1]):
            self.__create_new_scope(List[-1])
            return
        List.append(list())

    
    def __add_variable(self, type = False):
        if type : Type = type
        else: Type = self.__current_token.data
        
        self.__next_token()
        if self.__current_token.type != TokensTypes.identifier.value and self.__current_token.type != TokensTypes.functions.value: return
        self.__current_token.add_declared_type(Type)
        self.__add_token(self.__scope)
        
        previous_token = self.__current_token
        self.__next_token()
        if self.__current_token.type == TokensTypes.assignment_operator.value: 
            self.__find_valid_token()
            if not self.__check_assignment(previous_token, self.__current_token) : 
                self.__error_log.add_invalid_assignment(self.__current_token, previous_token.declared_type)
            self.__next_token() 
        if self.__current_token.type == TokensTypes.separator.value : self.__add_variable(type=Type)

    def __check_assignment(self, identifier, assignment):
        response_type = Types.what_type(assignment.data) 
        if response_type == identifier.declared_type:
            return True
        if response_type == DeclaredType.integer.value and identifier.declared_type == DeclaredType.floating.value:
            return True
        return False