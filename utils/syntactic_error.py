from enum import Enum, auto
from utils.token import Token


class Sintactic_error:
    def __init__(self) -> None:
        self.__errors = list()
    
    def print(self): 
        if len(self.__errors) == 0: return
        for erro in self.__errors:
            print(erro)

    def add_generic_error(self, token):
        self.__errors.append("[ERRO] -> Um erro inexperado ocorreu na linha {}. Referencia não definida para {}.".format(token.line, token.data))
    def add_unspected_token(self, token, expected, expected_type):
        self.__errors.append("[ERRO] -> Sintaxe inválida: Verifique a linha {}, esperado um(a) {} ({}) no lugar de {}.".format(
            token.line,
            expected_type,
            expected,
            token.data
        ))
    def add_missing_final_delimiter(self, token):
        self.__errors.append("[ERRO]-> Delimitador ausente: Esperado um ';' ao final da linha {}.".format(token.line))
    def add_unspected_type(self, token, expected):
        self.__errors.append("[ERRO]-> Linha: {} Esperado um {} no lugar de {}".format(token.line,expected, token.data))

        

    '''
    def __init__(self, *args) -> None:
        self.__len_args = len(args)
        if(self.__len_args > 0):
            self.__line = args[0]
        if(self.__len_args == 4):
            self.__current_token  = args[1]
            self.__expected_token = args[2]
            self.__expected_type  = args[3]

    def __generic_error(self):
        print("Há um erro detectado na linha {}".format(self.__line))
    def __expected_other(self):
        print("[ERRO] -> Sintaxe inválida: Na linha {} é esperado um {}: {} ao invés de: {}".format(
            self.__line, 
            self.__expected_type, 
            self.__expected_token, 
            self.__current_token))


    def print_erro(self):
        if(self.__len_args == 1): self.__generic_error()
        if(self.__len_args == 4): self.__expected_other()
    '''