from enum import Enum

class TokenTipo(Enum):

# delimitadores   
    FIM_DO_TEXTO = 03,      # 'ETX'
    NOVA_LINHA = 10,        # 'LF'

# operadores:
    ATRIBUICAO = 11,        # '='

# operadores aritméticos:
    ADICAO = 21             # (+)
    SUBTRACAO = 22          # (-)
    MULTIPLICACAO = 23      # (*)
    DIVISAO_INTEIRA = 24    # (/)
    RESTO_DIVISAO = 25      # (%)

# operadores relacionais:
    IGUAL_A = 31            # (==)
    DIFERENTE_DE = 32       # (!=)
    MAIOR_QUE = 33          # (>)
    MENOR_QUE = 34          # (<)
    MAIOR_OU_IGUAL_A = 35   # (>=)
    MENOR_OU_IGUAL_A = 36   # (<=)

# identificadores:
    VARIAVEIS = 41          # var

# constantes:
    CONST_NUM = 51          # int

# palavras reservadas:
    REM = 61                # comentarios
    INPUT = 62
    LET = 63                # atribui valor para var
    PRINT = 64              # output
    GOTO = 65               # salta para linha
    IF = 66                 # condicional
    END = 67                # encerra fonte