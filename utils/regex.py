import re

class RegexManagement:
    def __get_arithimetic_operator(self):
        return r'\+|-|\*|/|%'
    def __get_logic_operator(self):
        return r'==|>=|<=|!=|!|<|>'
    def __get_assignment_operator(self):
        return r'='
    def __get_delimiter(self):
        return r'\(|\)|{|}|\[|]|;'
    def __get_library(self):
        return r'\.h$'