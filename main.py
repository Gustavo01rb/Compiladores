from analysis.lexical import Lexical
from analysis.syntax import Sintax
from analysis.semantic import Semantic

#file_name = "inputs/Código 4.txt"

def main(file_name):
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()

    analisador_sintatico = Sintax(analisador_lexico.tokens)
    analisador_sintatico.analyze(print=True)

    analisador_semantico = Semantic(analisador_lexico.tokens)
    analisador_semantico.analyze()

    return 0

for i in range(10):
    file_name = "inputs/Código " + str(i+1) + ".txt"
    main(file_name)

