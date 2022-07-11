from utils.token import Token
from utils.C_rules import C_RESERVED_WORD
from utils.enumClass import TokensTypes

class Converter:
    def __init__(self, list_tokens) -> None:
        self.__tokens = list_tokens
        self.__current_index = 0
        self.__current_token = list_tokens[0]

    def start(self):
        self.__remove_unnecessary()
        self.__current_index = 0
        self.__current_token = self.__tokens[0]
        self.__analyse()
        self.__write_file()
    
    def __next_token(self): 
        self.__current_index += 1
        if self.__current_index >= len(self.__tokens)-1:
            self.__current_token = self.__tokens[-1]
            return
        self.__current_token = self.__tokens[self.__current_index]
    
    def __remove_token(self):
        if self.__current_index >= len(self.__tokens) - 1:
            self.__current_index = len(self.__tokens)-2
        self.__tokens.remove(self.__current_token)
        self.__current_token = self.__tokens[self.__current_index]

    def __remove_unnecessary(self):
        while self.__current_index != len(self.__tokens):
            if self.__current_token.type == TokensTypes.reserved_word.value: 
                self.__remove_unnecessary_case_reserved_word()
                continue
            if self.__current_token.type == TokensTypes.delimiter.value:
                self.__remove_unnecessary_case_delimiter()
                continue 
            self.__next_token()
        
    def __remove_unnecessary_case_reserved_word(self):
        if self.__current_token.data in C_RESERVED_WORD.directives():
            current_line = self.__current_token.line
            while current_line == self.__current_token.line:
                self.__remove_token()
            return
        if self.__current_token.data in C_RESERVED_WORD.type_declaration():
            if self.__tokens[self.__current_index+1].type == TokensTypes.functions.value:
                self.__current_token.data = "def"
                self.__next_token()
                return
            if self.__tokens[self.__current_index+2].data != "=":
                if self.__tokens[self.__current_index+1].data == ")":
                    self.__current_token = self.__tokens[self.__current_index - 1]
                    self.__current_index -= 1
                    self.__remove_token()
                    self.__remove_token()
                    self.__remove_token()
                    return
                current_line = self.__current_token.line
                while current_line == self.__current_token.line:
                    self.__remove_token()
                return
            self.__remove_token()
        self.__next_token()

    def __remove_unnecessary_case_delimiter(self):
        if self.__current_token.data == "(" or self.__current_token.data == ")" or self.__current_token.data == "}": self.__next_token()
        if self.__current_token.data == ";": 
            self.__remove_token()
            return
        if self.__current_token.data == "{":
            self.__current_token.data = ":"
            self.__current_token.line -= 1
            self.__next_token() 

    def __analyse(self):
        while self.__current_index != len(self.__tokens):
            if self.__current_token.data in C_RESERVED_WORD.functions():
                self.__convert_function()
                continue
            self.__next_token()

    def __convert_function(self):
        if self.__current_token.data == "scanf":
            type_input = ""
            name = self.__tokens[self.__current_index+5].data
            if self.__tokens[self.__current_index+2].data == "\"%i\"": type_input = "int"
            if self.__tokens[self.__current_index+2].data == "\"%f\"": type_input = "float"
            current_line = self.__current_token.line
            self.__current_token.data = name + " = " + type_input + "(input(" + "))" 
            self.__next_token()
            while current_line == self.__current_token.line:
                self.__remove_token()

    
    def __write_file(self):
        tabulacao = 0
        file = open("outputs/teste/tese.py", "w")
        file.close()
        file = open("outputs/teste/tese.py", "a")
        current_line = self.__tokens[0].line;
        for iterator in self.__tokens:
            if iterator.data == ":":
                tabulacao += 1
            if iterator.data == "}":
                tabulacao -= 1
                continue
            if current_line != iterator.line:
                file.write("\n")
                current_line = iterator.line
                for count in range(tabulacao):
                    file.write("\t")
            file.write(iterator.data + " ")
        file.write("\n\nmain()")