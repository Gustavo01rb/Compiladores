from unicodedata import name
from symbols import Symbols

class Lexico:

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__validate_file_name()
        self.__tokens = []

    @property
    def tokens(self):
        return self.__tokens
    
    #Função que valida a exitência do arquivo
    def __validate_file_name(self):
        try:
            self.__content = open(self.__file_name, "r")
        except:
            raise ValueError("Falha ao abrir o arquivo {}, verifique se o mesmo existe!".format(self.__file_name))

    def add_token(self,token, type, line):
        self.__tokens.append({
            "token" : token,
            "type"  : type,
            "line"  : line 
        })            

    def __analyse_token(self, response, expression, line):
        operator           = response["match"][0]        # Pegando o operador a ser analisado 
        position_operator  = expression.find(operator)   # Pegando a posição do primeiro operador lógico da expressão 

        if expression == operator:
            self.add_token(operator, response["type"], line)
            return


        if position_operator > 0:
            self.__validate_token(expression[:position_operator], line)             # Verificando o conteúdo que vem antes do operador
            
        self.add_token(operator, response["type"], line)                            # Adiciona o operador a lista de tokens
        self.__validate_token(expression[position_operator + len(operator):], line) # Analisa partes depois do operador


    def __validate_token(self, token, line):

        if token == "" or token == None: return #Verificação de palavra vazia
        symbols = Symbols()
        
        #Verificando se é palavra reservada 
        result = symbols.is_reserved_word(token)
        if result:
            self.add_token(token, result["type"], line) 
            return
        
        #Verificando se há operadores lógicos
        result = symbols.is_logic_operator(token)
        if result:
            self.__analyse_token(result, token, line)
            return
        
        #Verificando se há Delimitadores
        result = symbols.is_delimiter(token)
        if result:
            self.__analyse_token(result, token, line)
            return
        
        #Verificando se há operador atitmético
        result = symbols.is_arithimetic_operator(token)
        if result:
            self.__analyse_token(result, token, line)
            return      
        
        #Verificando se há Atribuição de igualdade
        result = symbols.is_assignment_operator(token)
        if result:
            self.__analyse_token(result, token, line)
            return    

        if token.isnumeric():
            self.add_token(token, symbols.numeric_constant, line)
            return
        
        self.add_token(token, symbols.identifier, line)
        return


    #Função que gerencia a tokenização
    def tokenization(self):
        for index, line in enumerate(self.__content):
            line = line.strip() # Função que retira os espaços desnecesários ao final e início da string
            line = line.split() # Função que separa as stirngs. Nesse caso com base em " "
            for iterator in line:
                iterator = iterator.strip()
                self.__validate_token(iterator, index)
        self.__final_chek()

    def __final_chek(self):
        symbols = Symbols()
        for index, iterator in enumerate(self.__tokens):
            if symbols.is_library(iterator["token"]):
                iterator['type'] = symbols.library
                if(self.__tokens[index-1]['type'] == symbols.logic_operator):
                    self.__tokens[index-1]['type'] = symbols.delimiter
                if(self.__tokens[index+1]['type'] == symbols.logic_operator):
                    self.__tokens[index+1]['type'] = symbols.delimiter


    def print_tokens(self):
        print("\nTokens obtidos:")
        for iterator in self.__tokens:
            print("{:>10} - {}".format(iterator['token'], iterator['type']))
        print("\n\nQuantidade de Tokens: {} \n".format(len(self.__tokens)))
        