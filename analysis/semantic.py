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
               self.__current_token.type != TokensTypes.txt.value              and 
               self.__current_token.type != TokensTypes.character.value        and
               self.__current_token.data != ";"
               ): 
            self.__next_token()
    
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
            return
        if self.__current_token.data in C_RESERVED_WORD.type_declaration():
            self.__add_variable()
            return
        if self.__current_token.type == TokensTypes.identifier.value:
            self.__case_identifier()
            return
        if self.__current_token.data == "}":
            self.__exclude_scope(self.__scope)
            return
    
    def __create_new_scope(self, List):
        if not List: return
        if Types.is_list(List[-1]):
            self.__create_new_scope(List[-1])
            return
        List.append(list())
    def __exclude_scope(self, List):
        if not List: return
        if Types.is_list(List[-1]):
            if self.__exclude_scope(List[-1]):
                List.pop()
        else: return True
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
            if self.__current_token.data == ";": return
            if not self.__check_assignment(previous_token, self.__current_token) : 
                self.__error_log.add_invalid_assignment(self.__current_token, previous_token.declared_type)
            self.__next_token() 
        if self.__current_token.type == TokensTypes.separator.value : self.__add_variable(type=Type)
    
    def __case_identifier(self):
        if not self.__search_token_in_scope(self.__current_token, self.__scope):
            self.__error_log.add_identifier_not_in_scope(self.__current_token)
            return
        initial_token = self.__current_token
        self.__next_token()
        if self.__current_token.type == TokensTypes.assignment_operator.value:
            self.__check_expression(initial_token)

    def __check_assignment(self, identifier, assignment):
        response_type = Types.what_type(assignment.data) 
        if response_type == identifier.declared_type:
            return True
        if response_type == DeclaredType.integer.value and identifier.declared_type == DeclaredType.floating.value:
            return True
        return False
    
    def __check_expression(self, initial_token):
        while self.__current_token.data != ";":
            self.__find_valid_token()
            if self.__current_token.data == ";": return
            if self.__current_token.type == TokensTypes.identifier.value:
                if not self.__search_token_in_scope(self.__current_token, self.__scope):
                    self.__error_log.add_identifier_not_in_scope(self.__current_token)
                    break
                if initial_token.declared_type != self.__current_token.declared_type :
                    if ( initial_token.declared_type == DeclaredType.floating.value and 
                     self.__current_token.declared_type == DeclaredType.integer.value): pass
                    else: self.__error_log.add_invalid_assignment(self.__current_token, initial_token.declared_type)
            elif Types.what_type(self.__current_token.data) != initial_token.declared_type:
                if ( Types.what_type(self.__current_token.data) == DeclaredType.integer.value and 
                     initial_token.declared_type == DeclaredType.floating.value): pass
                else: self.__error_log.add_invalid_assignment(self.__current_token, initial_token.declared_type)
            self.__next_token()
            if self.__current_token.data == "/":
                if self.__tokens[self.__current_index + 1].data == "0":
                    self.__error_log.error_division_by_zero(self.__tokens[self.__current_index + 1])
                
            
    
    def __search_token_in_scope(self, token, scope):
        for iterator in scope:
            if Types.is_list(iterator): return self.__search_token_in_scope(token, iterator)
            if token.data == iterator.data:
                token.declared_type = iterator.declared_type
                return True
        return False