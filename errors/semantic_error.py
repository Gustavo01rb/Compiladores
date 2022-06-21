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
        self.__errors.append("[ERRO]-> Atribuição inválida. {} não corresponde ao tipo {}".format(token.data, expected))