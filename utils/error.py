class Error:
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