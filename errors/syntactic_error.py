class Sintactic_error:
    def __init__(self) -> None:
        self.__errors = list()
    
    def print(self): 
        file = open('outputs/sintax.txt','a')
        if len(self.__errors) == 0: 
            file.write("Não foram encontrados erros sintáticos\n")
            print("\nNão foram encontrados erros sintáticos\n\n")
            return
        for erro in self.__errors:
            print(erro)
            file.write(erro + "\n")
        file.close()
        
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