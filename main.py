from analysis.lexical import Lexical
from analysis.syntax import Sintax
from analysis.semantic import Semantic

def main(file_name):
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()

    analisador_sintatico = Sintax(analisador_lexico.tokens, file_name)
    analisador_sintatico.analyze(print=True)

    analisador_semantico = Semantic(analisador_lexico.tokens, file_name)
    analisador_semantico.analyze()

    return 0

for i in range(10):
    file_name = "Código " + str(i+1) + ".txt"
    main(file_name)

