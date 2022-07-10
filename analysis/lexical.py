import io, os
from utils.enumClass import DeclaredType, RegexStructure, TokensTypes, TokenStructure
from utils.token import Token
import re

from utils.types import Types

class Lexical:
    def __init__(self, file_name) -> None:
        self.__file_name = file_name
        self.__validate_file_name()
        self.__tokens = list()

    def __validate_file_name(self):
        try:
            directory = "inputs/" + self.__file_name
            self.__content_file = open(directory, "r")
        except:
            raise ValueError("Falha ao abrir o arquivo {}, verifique se o mesmo existe!".format(self.__file_name))
     
    @property
    def tokens(self): return self.__tokens

    def __remove_coments(self):
        output  = io.BytesIO()
        wrapper = io.TextIOWrapper(
            output,
            encoding='cp1252',
            line_buffering=True,)

        for line in self.__content_file:
            line = line.split("//") # Função que separa as stirngs. Nesse caso com base em " "
            line = line[0]+'\n'
            wrapper.write(line)
        
        self.__content_file = wrapper
        

        

    def tokenization(self):  #Método que gerencia a tokenização
        self.__remove_coments()
        
        self.__content_file.seek(0,0)
        for index, line in enumerate(self.__content_file.readlines()):
            line = line.strip() # Função que retira os espaços desnecesários ao final e início da string
            line = line.split() # Função que separa as stirngs. Nesse caso com base em " "
            for iterator in line:
                iterator = iterator.strip()
                self.__validate_token(iterator, index)
        self.__separate_identifier()

    def __validate_token(self, token, line):
        if token == "" or token == None: return #Verificação de palavra vazia
        parsed_token = self.__analyse_token(token)
        
        if not parsed_token[TokenStructure.match.value]:
            self.__tokens.append(
                Token( 
                parsed_token[TokenStructure.data.value], 
                parsed_token[TokenStructure.type.value],
                line))
            return
        self.__token_handling(parsed_token, line)
        return

    def __token_handling(self, parsed_token, line):
        operator           = parsed_token[TokenStructure.match.value][0]            # Pegando o operador a ser analisado 
        position_operator  = parsed_token[TokenStructure.data.value].find(operator) # Pegando a posição do primeiro operador lógico da expressão 

        if parsed_token[TokenStructure.data.value] == operator:
            self.__tokens.append(
                Token(
                    operator, 
                    parsed_token[TokenStructure.type.value], 
                    line))
            return


        if position_operator > 0:
            self.__validate_token(parsed_token[TokenStructure.data.value][:position_operator], line)   # Verificando o conteúdo que vem antes do operador
        
        self.__tokens.append(
                Token(
                    operator, 
                    parsed_token[TokenStructure.type.value], 
                    line))
        self.__validate_token(parsed_token[TokenStructure.data.value][position_operator + len(operator):], line) # Analisa partes depois do operador


    def __analyse_token(self, token):
        if token.isnumeric() or Types.what_type(token) == DeclaredType.floating.value:
            return{
                TokenStructure.type.value  : TokensTypes.numeric_constant.value,
                TokenStructure.match.value : False,
                TokenStructure.data.value  : token
            }

        for index, itererator in enumerate(RegexStructure):
            if index == 0:
                if token in itererator.value:
                    return{
                        TokenStructure.type.value  : TokensTypes.reserved_word.value,
                        TokenStructure.match.value : False,
                        TokenStructure.data.value  : token
                    }
                continue

            if re.findall(itererator.value[0], token):
                 return{
                        TokenStructure.type.value  : itererator.value[1],
                        TokenStructure.match.value : re.findall(itererator.value[0], token),
                        TokenStructure.data.value  : token
                    }

        return{
            TokenStructure.type.value  : TokensTypes.identifier.value,
            TokenStructure.match.value : False,
            TokenStructure.data.value  : token
        }
    
    def __separate_identifier(self):
        for index, iterator in enumerate(self.__tokens):
            if iterator.type == TokensTypes.identifier.value:
                if self.__tokens[index+1].data == "(":
                    iterator.type = TokensTypes.functions.value
                    continue
            elif iterator.type == TokensTypes.library.value:
                if self.__tokens[index-1].data == "<":
                    self.__tokens[index-1].type = TokensTypes.delimiter.value
                if self.__tokens[index+1].data == ">":
                    self.__tokens[index+1].type = TokensTypes.delimiter.value

    def print_tokens(self):
        directory = "outputs/lexical/" + self.__file_name 
        file = open(directory,'w')
        
        print("\nTokens obtidos:")
        file.write("\nTokens obtidos na análise léxica:\n\n")
        
        print("-------------------------------------------------")
        file.write("-------------------------------------------------\n")
        
        print("|{:^10} | {:^25} | {:^3} |".format("Token", "Tipo", "Linha"))
        file.write("|{:^10} | {:^25} | {:^3} |\n".format("Token", "Tipo", "Linha"))
        
        print("-------------------------------------------------")
        file.write("-------------------------------------------------\n")
        
        for iterator in self.__tokens:
            print("|{:>10} | {:<25} | {:^5} |".format(iterator.data, iterator.type, iterator.line))
            file.write("|{:>10} | {:<25} | {:^5} |\n".format(iterator.data, iterator.type, iterator.line))

        print("-------------------------------------------------")
        file.write("-------------------------------------------------\n")
        
        print("\n\nQuantidade de Tokens: {} \n".format(len(self.__tokens)))
        file.write("\n\nQuantidade de Tokens: {}".format(len(self.__tokens)))
        file.close()