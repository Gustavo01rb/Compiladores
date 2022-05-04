from lexico import Lexico
from symbols import Symbols
import re

file_name = "arquivo.txt"

def main():
    analisador_lexico = Lexico(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()
    return 0

main()