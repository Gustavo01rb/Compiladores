import re
class Lexico:

    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__tokens = []
        self.__validated_tokens = []
        self.__validate_file_name()
        self.__reservede_word = ["const", "while", "for", "if", "#include", "<stdio.h>", "<stdlib.h>", "do", "return", "int", "string", "float", "double", "bool", ";"]
        self.__regx_operator = re.compile("[/*-+%!]")
        self.__regx_delimiter = re.compile("[\{\}()]")

        

    def reserved(self, expression):
        return (expression in self.__reservede_word)
    def number(self, expression):
        return re.search("\d", expression)
    def delimiters(self, expression):
        search_symbol = self.__regx_delimiter.search(expression)
        if search_symbol:
            return search_symbol.group()
        return False

    def operators(self, expression):
        search_symbol = self.__regx_operator.search(expression)
        if search_symbol:
            return search_symbol.group()
        return False


    #função que valida a exitência do arquivo
    def __validate_file_name(self):
        try:
            self.__content = open(self.__file_name, "r")
        except:
            raise ValueError("Falha ao abrir o arquivo, verifique se o mesmo existe!")
    
    def __case_parenthesis(self, iterator):
        if(len(iterator) == 1):
            self.__tokens.append("(")
            return

        iterator = iterator.split("(")
        if(iterator[0] != ''): self.__tokens.append(iterator[0])
        self.__tokens.append("(")

        if(len(iterator[1]) > 1):     
            iterator[1] = iterator[1].split(")")

            if(iterator[1][0] != ''): 
                contain_operator = self.operators(iterator[1][0])
                if not contain_operator:
                    self.__tokens.append(iterator[1][0])
                else:
                    expression = iterator[1][0]
                    if(expression[0] == contain_operator): return Exception
                    expression = expression.split(contain_operator)
                    self.__tokens.append(expression[0])
                    self.__tokens.append(contain_operator)
                    self.__tokens.append(expression[1]) 

            self.__tokens.append(")")
            self.__tokens.append(iterator[1][1])
            return

    
    def __case_end_line(self, iterator):
        iterator = iterator.split(";")
        self.__tokens.append(iterator[0])
        self.__tokens.append(";")

    
    def tokenization(self):
        try:
            for line in self.__content:
                line = line.strip() # Função que retira os espaços desnecesários ao final e início da string
                list_aux = line.split() # Função que separa as stirngs. Nesse caso com base em " "
                for iterator in list_aux:
                    iterator = iterator.strip()
                    if(";" in iterator):
                        self.__case_end_line(iterator)
                        continue
                    if("(" in iterator):
                        if(self.__case_parenthesis(iterator) == Exception):
                            raise Exception
                        continue
                    
                    self.__tokens.append(iterator)

        except:
            raise Exception("Algo errado ocorreu com a tokenização.")
        
        
    def validate_token(self):
        i = -1
        while(i < len(self.__tokens) -1 ) :
            i += 1

            if(self.reserved(self.__tokens[i])):
                self.__validated_tokens.append([self.__tokens[i], "Palavra reservada"])
                continue
            if(self.operators(self.__tokens[i])):
                self.__validated_tokens.append([self.__tokens[i], "Operador"])
                continue
            if(self.__tokens[i] == "="):
                self.__validated_tokens.append([self.__tokens[i], "Atribuição"])
                continue
            if(self.number(self.__tokens[i])):
                self.__validated_tokens.append([self.__tokens[i], "Constante numérica"])
                continue
            if(self.delimiters(self.__tokens[i])):
                self.__validated_tokens.append([self.__tokens[i], "Delimitador"])
                continue
            if(self.__tokens[i+1] == "("):
                self.__validated_tokens.append([self.__tokens[i], "Nome de função"])
                continue
            if("\"" in self.__tokens[i]):
                aux = self.__tokens[i]
                while( aux.count("\"") < 2 ):
                    aux = aux + " " + self.__tokens[i+1]
                    i += 1
                self.__validated_tokens.append([aux, "Literal"])
                continue
            self.__validated_tokens.append([self.__tokens[i], "Variável"])
            

                
    
    def print_tokens(self):
        for iterator in self.__validated_tokens:
            print("{}\t\t -> {}".format(iterator[0], iterator[1]))        

    def teste(self):
        for x in self.__tokens:
            print(x)