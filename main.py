from analysis.lexical import Lexical
from analysis.syntax import Sintax


file_name = "inputs/simple_calculator.txt"

def main():
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()

    analisador_sintatico = Sintax(analisador_lexico.tokens)
    analisador_sintatico.analyze(print=True)


    


    return 0

main()
