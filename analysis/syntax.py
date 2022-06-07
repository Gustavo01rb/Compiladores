from utils.token import Token
from utils.enumClass import TokensTypes
from utils.C_rules import C_RESERVED_WORD
from utils.error import Error


class Sintax:
    def __init__(self, listToken) -> None:
        self.__tokens = listToken
        self.__current_index = 0
        self.__current_index_content = listToken[0].data
        self.__current_index_type = listToken[0].type
        self.__error_log = Error()

    #Função de movimentação nos Tokens
    def __next_token(self):
        self.__current_index += 1
        self.__current_index_content = self.__tokens[self.__current_index].data
        self.__current_index_type = self.__tokens[self.__current_index].type

    #Funções para criação dos erros
    def __update_error_log(self, current_token, expected_token, expected_type):
        if(expected_token != None):
            self.__error_log = Error(self.__tokens[self.__current_index].line, current_token, expected_token, expected_type)
            return
        self.__error_log = Error(self.__tokens[self.__current_index].line)
        
    def analyze(self):
        while(self.__current_index < len(self.__tokens)):
            erro = self.__analyze_sentence()
            if not erro: continue
            self.__error_log.print_erro()
            break


    def __analyze_sentence(self):
        token_type = self.__tokens[self.__current_index].type

        if    token_type == TokensTypes.reserved_word.value: return self.__case_reserved_word()
        elif  token_type == TokensTypes.functions.value:     return self.__case_function()
        elif  token_type == TokensTypes.identifier.value:    return False
        else: 
            print("Erro")
            return True

    #Caso de palavras reservadas
    def __case_reserved_word(self):
        if self.__current_index_content in C_RESERVED_WORD.directives(): 
            return self.__case_reserved_word_directives()
        if self.__current_index_content in C_RESERVED_WORD.type_declaration():
            return self.__case_reserved_word_declaration_type()
    
    #Caso de palavras reservadas - Diretivas
    def __case_reserved_word_directives(self):
        if(self.__current_index_content == "#include"): #q9
            self.__next_token()
            if(self.__current_index_content != '<'): #q10
                self.__update_error_log(self.__current_index_content,'<', TokensTypes.delimiter.value)
                return True
            self.__next_token()
            if(self.__current_index_type != TokensTypes.library.value): #q11 
                self.__update_error_log(self.__current_index_content,'.h', TokensTypes.library.value)
                return True
            self.__next_token()
            if(self.__current_index_content != '>'): #q12
                self.__update_error_log(self.__current_index_content,'>', TokensTypes.delimiter.value)
                return True
            self.__next_token()
            
        return False
    
    def __case_reserved_word_declaration_type(self):
        self.__next_token()
        if    self.__current_index_type == TokensTypes.functions.value:  return self.__case_function()
        elif  self.__current_index_type != TokensTypes.identifier.value:
            print("Entrou") 
            self.__update_error_log(self.__current_index_content," ", TokensTypes.identifier.value)
            return True
        


    #Caso Funções
    def __case_function(self):
        self.__next_token()
        if self.__current_index_content != '(':
            self.__update_error_log(self.__current_index_content,'(', TokensTypes.delimiter.value)
            return True

        self.__next_token()
        if self.__current_index_content != ')': self.__analyze_sentence()
        if self.__current_index_content != ')':
            self.__update_error_log(self.__current_index_content,')', TokensTypes.delimiter.value)
            return True

        self.__next_token()
        if self.__current_index_content != '{':
            self.__update_error_log(self.__current_index_content,'{', TokensTypes.delimiter.value)
            return True

        self.__next_token()
        if self.__current_index_content != '}': self.__analyze_sentence()
        if self.__current_index_content != '}': 
            self.__update_error_log(self.__current_index_content,'}', TokensTypes.delimiter.value)
            return True
        self.__next_token()
        return False



