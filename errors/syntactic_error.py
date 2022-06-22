class Sintactic_error:
    def __init__(self, file_name) -> None:
        self.__errors = list()
        self.__file_name = file_name
    
    def print(self): 
        directory = "outputs/syntax/" + self.__file_name
        file = open(directory,'w')
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