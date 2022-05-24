from analysis.lexical import Lexical


file_name = "inputs/simple_calculator.txt"

def main():
    analisador_lexico = Lexical(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.print_tokens()


    


    return 0

main()
