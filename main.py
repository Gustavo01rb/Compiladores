from analysis.lexical import Lexical
from analysis.syntax import Sintax
from analysis.semantic import Semantic
from converter.converter import Converter

def main(file_name):
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    #analisador_lexico.print_tokens()

    #analisador_sintatico = Sintax(analisador_lexico.tokens, file_name)
    #analisador_sintatico.analyze(print=True)

    #analisador_semantico = Semantic(analisador_lexico.tokens, file_name)
    #analisador_semantico.analyze()

    converter = Converter(analisador_lexico.tokens)
    converter.start()
    return 0

#for i in range(10):
 #   file_name = "código" + str(i+1) + ".txt"
#  main(file_name)
main("código1.txt")
