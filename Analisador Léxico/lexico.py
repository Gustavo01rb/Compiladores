from unicodedata import name
from symbols import Symbols

class Lexico:

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__validate_file_name()
        self.__tokens = []
    
    #Função que valida a exitência do arquivo
    def __validate_file_name(self):
        try:
            self.__content = open(self.__file_name, "r")
        except:
            raise ValueError("Falha ao abrir o arquivo {}, verifique se o mesmo existe!".format(self.__file_name))

    def add_token(self,token, type):
        self.__tokens.append({
            "token" : token,
            "type"  : type 
        })            

    def __case_logic_operator(self, response, expression):
        operator           = response["match"][0]        # Pegando o operador a ser analisado 
        position_operator  = expression.find(operator)   # Pegando a posição do primeiro operador lógico da expressão 

        if expression == operator:
            self.add_token(operator, response["type"])
            return


        if position_operator > 0:
            self.__analyse_token(expression[:position_operator])             # Verificando o conteúdo que vem antes do operador
            
        self.add_token(operator, response["type"])                           # Adiciona o operador a lista de tokens
        self.__analyse_token(expression[position_operator + len(operator):]) # Analisa partes depois do operador






    def __analyse_token(self, token,):

        if token == "" or token == None: return #Verificação de palavra vazia

        symbols = Symbols()
        result = symbols.is_reserved_word(token)
        
        #Verificando se é palavra reservada 
        if result:
            self.add_token(token, result["type"]) 
            return
        
        #Verificando se há operadores lógicos
        result = symbols.is_logic_operator(token)
        if result:
            self.__case_logic_operator(result, token)
          




        
    
    #Função que gerencia a tokenização
    def tokenization(self):
        for line in self.__content:
            line = line.strip() # Função que retira os espaços desnecesários ao final e início da string
            line = line.split() # Função que separa as stirngs. Nesse caso com base em " "
            for iterator in line:
                iterator = iterator.strip()
                self.__analyse_token(iterator)



    def print_tokens(self):
        print("\nTokens obtidos:")
        for iterator in self.__tokens:
            print("{:>10} -> {}".format(iterator['token'], iterator['type']))
        print("\n\nQuantidade de Tokens: {} \n".format(len(self.__tokens)))
        