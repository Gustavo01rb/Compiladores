class Semantic_error:
    def __init__(self) -> None:
        self.__errors = list()
    
    def print(self): 
        file = open('outputs/semantic.txt','w')
        if len(self.__errors) == 0: 
            file.write("Não foram encontrados erros semânticos")
            print("\nNão foram encontrados erros semânticos\n\n")
            return
        for erro in self.__errors:
            print(erro)
            file.write(erro + "\n")
        file.close()

    def add_invalid_assignment(self, token, expected):
        self.__errors.append("[ERRO]-> Atribuição inválida. Linha {}, {} não corresponde ao tipo {}".format(token.line,token.data, expected))
    
    def add_identifier_not_in_scope(self, token):
        self.__errors.append("[ERRO]-> Variável não declarda. Linha {}, {} não declarado ou não existe.".format(token.line,token.data))
    
    def error_division_by_zero(self,token):
        self.__errors.append("[ERRO]-> Divisão por zero. Linha {}, não é possível realizar essa operação.".format(token.line,token.data))

