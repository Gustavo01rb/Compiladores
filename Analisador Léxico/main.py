from lexico import Lexico

file_name = "arquivo.txt"

def main():
    analisador_lexico = Lexico(file_name)
    analisador_lexico.tokenization()
    analisador_lexico.validate_token()
    analisador_lexico.print_tokens()
    return 0

main()