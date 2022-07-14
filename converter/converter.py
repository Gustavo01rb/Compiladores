from utils.token import Token
from utils.C_rules import C_RESERVED_WORD
from utils.enumClass import TokensTypes

class Converter:
    def __init__(self, list_tokens, file_name) -> None:
        self.__tokens = list_tokens
        self.__current_index = 0
        self.__current_token = list_tokens[0]
        self.__file_name = file_name
        self.__add_line = 0

    #Funções utilitárias
    def __next_token(self): 
        self.__current_index += 1
        if self.__current_index >= len(self.__tokens)-1:
            self.__current_token = self.__tokens[-1]
            return
        self.__current_token = self.__tokens[self.__current_index]
        self.__current_token.line += self.__add_line
    
    def __previous_token(self): 
        self.__current_index -= 1
        if self.__current_index < 0:
            self.__current_token = self.__tokens[0]
            return
        self.__current_token = self.__tokens[self.__current_index]
    
    def __remove_token(self):
        self.__current_token.data = None
        self.__current_token.type = TokensTypes.library
    
    def __remove_line(self):
        current_line = self.__current_token.line
        while current_line == self.__current_token.line:
            self.__remove_token()
            self.__next_token()
        self.__previous_token()
    
    #Função principal
    def start(self):
        while self.__current_index != len(self.__tokens):
            self.__convert_functions()
            self.__check_need()
            self.__next_token()
        self.__write_file()

    #Funções que checam se há necessidade do token na linguagem Python
    def __check_need(self):
        if   self.__current_token.type == TokensTypes.reserved_word.value: 
            self.__check_need_case_reserved_word()
        elif self.__current_token.type == TokensTypes.delimiter.value:
            self.__check_need_case_delimiter()
        elif self.__current_token.type == TokensTypes.separator.value:
            self.__check_need_case_separator()
        elif self.__current_token.type == TokensTypes.identifier.value:
            self.__check_need_case_identifier()

    def __check_need_case_reserved_word(self):
        if self.__current_token.data in C_RESERVED_WORD.directives():
            self.__remove_line()
            return
        if self.__current_token.data in C_RESERVED_WORD.type_declaration():
            if self.__tokens[self.__current_index+1].type == TokensTypes.functions.value:
                self.__current_token.data = "def"
                return
            self.__remove_token()
    
    def __check_need_case_delimiter(self):
        if self.__current_token.data == "(":
            if self.__tokens[self.__current_index+1].data in C_RESERVED_WORD.type_declaration():
                if self.__tokens[self.__current_index+2].data == ")": #Caso de casting
                    self.__remove_token()
                    self.__next_token()
                    self.__remove_token()
                    self.__next_token()
                    self.__remove_token()
                    self.__next_token()
        elif self.__current_token.data == "{":
            self.__current_token.data = ":"
            self.__current_token.line = self.__tokens[self.__current_index-1].line  
        elif self.__current_token.data == ";":
            self.__remove_token()
    
    def __check_need_case_separator(self):
        current_line = self.__current_token.line
        index = 0
        while current_line == self.__current_token.line:
            index += 1 
            current_line = self.__tokens[self.__current_index - index].line
            if self.__tokens[self.__current_index - index].type == TokensTypes.functions.value: return
        self.__remove_token()
        self.__add_line += 1

    def __check_need_case_identifier(self):
        current_line = self.__current_token.line
        index = 0
        while current_line == self.__current_token.line:
            index += 1 
            current_line = self.__tokens[self.__current_index - index].line
            if self.__tokens[self.__current_index - index].type == TokensTypes.functions.value: return
        if self.__tokens[self.__current_index-1].type == TokensTypes.reserved_word.value:
            if self.__tokens[self.__current_index+1].type == TokensTypes.delimiter.value:
                self.__remove_token()
        if self.__tokens[self.__current_index-1].type == TokensTypes.separator.value:
            if self.__tokens[self.__current_index+1].type == TokensTypes.separator.value:
                self.__remove_token()    
        if self.__tokens[self.__current_index-1].type == TokensTypes.separator.value:
            if self.__tokens[self.__current_index+1].type == TokensTypes.delimiter.value:
                self.__remove_token() 

    def __convert_functions(self):
        if not self.__current_token.data in C_RESERVED_WORD.functions(): return
        if self.__current_token.data == "for":
            self.__next_token()#(
            self.__remove_token()
            self.__next_token()#int
            self.__remove_token()
            self.__next_token()#i
            self.__next_token()#=
            self.__current_token.data = "in"
            self.__next_token()#0
            self.__current_token.data = "range"
            self.__next_token()#;
            self.__current_token.data = "("
            self.__next_token()#i
            self.__remove_token()
            self.__next_token()#<
            self.__remove_token()
            self.__next_token()#valor
            self.__next_token()#;
            self.__current_token.data = ")"
            self.__next_token()#<
            self.__remove_token()
            self.__next_token()#<
            self.__remove_token()
            self.__next_token()#<
            self.__remove_token()
            return
        if self.__current_token.data == "scanf":
            type_input = ""
            name = self.__tokens[self.__current_index+5].data
            if self.__tokens[self.__current_index+2].data == "\"%i\"": type_input = "int"
            if self.__tokens[self.__current_index+2].data == "\"%f\"": type_input = "float"
            current_line = self.__current_token.line
            self.__current_token.data = name + " = " + type_input + "(input(" + "))" 
            self.__next_token()
            self.__remove_line() 
                    
    def __write_file(self):
        tabulation = 0
        file = open("outputs/converter/" + self.__file_name + ".py", "w")
        file.close()
        file = open("outputs/converter/" + self.__file_name + ".py", "a")
        current_line = self.__tokens[0].line;
        for iterator in self.__tokens:
            if iterator.data == None: continue
            if iterator.data == ":":
                tabulation += 1
            elif iterator.data == "}":
                tabulation -= 1
                continue
            if current_line != iterator.line:
                file.write("\n")
                current_line = iterator.line
                for count in range(tabulation):
                    file.write("\t")
            if iterator.type != TokensTypes.delimiter.value:
                file.write(iterator.data + " ")
            else:
                file.write(iterator.data)
                
        file.write("\n\nmain()")