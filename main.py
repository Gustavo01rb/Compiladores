from analysis.lexical import Lexical
from analysis.syntax import Sintax
from analysis.semantic import Semantic

file_name = "inputs/Código 1.txt"

def main():
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()

    analisador_sintatico = Sintax(analisador_lexico.tokens)
    analisador_sintatico.analyze(print=True)

    analisador_semantico = Semantic(analisador_lexico.tokens)
    analisador_semantico.analyze()

    return 0

main()
