class C_RESERVED_WORD:
    @staticmethod
    def all():
        return C_RESERVED_WORD.type_declaration() + C_RESERVED_WORD.functions() + C_RESERVED_WORD.directives() + C_RESERVED_WORD.returns()

    @staticmethod
    def type_declaration():
        return ["int", "float", "void", "doule", "char", "struct"]
    @staticmethod
    def functions():
        return ["if", "while", "else", "for", "do", "scanf", "fscaf", "fprintf", "fgets", "getc"]
    @staticmethod
    def directives():
        return ["#include", "#define", "#ifndef", "#endif", "#error"]
    @staticmethod
    def returns():
        return ["return"]